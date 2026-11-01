// Renderiza cada components/<Comp>/preview.html como o frame do Design System faria:
// tokens.css + bundle.css pré-carregados, <html data-theme="noite">, logo no lugar de /_blob/<id>.
// Uso: node render.js <dir-project> <dir-saida> [Comp ...]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [proj, outDir, ...only] = process.argv.slice(2);
const S = path.resolve(__dirname, '..');
fs.mkdirSync(outDir, { recursive: true });
const tmp = path.join(outDir, '_tmp');
fs.mkdirSync(tmp, { recursive: true });
fs.copyFileSync(path.join(S, 'render/logo.jpg'), path.join(tmp, 'logo.jpg'));
fs.copyFileSync(path.join(outDir, 'tokens.css'), path.join(tmp, 'tokens.css'));
fs.copyFileSync(path.join(proj, 'components/bundle.css'), path.join(tmp, 'bundle.css'));

(async () => {
  const browser = await chromium.launch();
  const comps = fs.readdirSync(path.join(proj, 'components'))
    .filter(d => fs.existsSync(path.join(proj, 'components', d, 'preview.html')))
    .filter(d => !only.length || only.includes(d));
  const report = [];
  for (const c of comps) {
    let html = fs.readFileSync(path.join(proj, 'components', c, 'preview.html'), 'utf8');
    const marker = html.split('\n')[0];
    const w = +(marker.match(/width=(\d+)/) || [0, 960])[1];
    const h = +(marker.match(/height=(\d+)/) || [0, 320])[1];
    html = html.replace(/\/_blob\/[0-9a-f]{32}/g, 'logo.jpg')
      .replace(/<html([^>]*)>/i, '<html$1 data-theme="noite">')
      .replace(/<head>/i, '<head><link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="bundle.css">');
    const f = path.join(tmp, c + '.html');
    fs.writeFileSync(f, html);
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    const errs = [];
    page.on('pageerror', e => errs.push(e.message));
    page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await page.goto('file://' + f);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(250);
    // Medidas: estouro horizontal do texto e da área útil
    const issues = await page.evaluate(() => {
      const out = [];
      const arte = document.querySelector('.ie-arte, .ie-painel, .cover');
      if (!arte) return out;
      const ar = arte.getBoundingClientRect();
      document.querySelectorAll('p,h1,h2,h3,span,li,div').forEach(el => {
        if (!el.childNodes.length) return;
        const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
        if (!hasText) return;
        const r = el.getBoundingClientRect();
        if (r.width === 0) return;
        if (el.scrollWidth > el.clientWidth + 2 && getComputedStyle(el).overflow !== 'visible')
          out.push(`transborda: "${el.textContent.trim().slice(0, 40)}"`);
        if (r.right > ar.right + 1 || r.left < ar.left - 1 || r.bottom > ar.bottom + 1)
          out.push(`fora da arte: "${el.textContent.trim().slice(0, 40)}" (${Math.round(r.left)},${Math.round(r.top)},${Math.round(r.right)},${Math.round(r.bottom)})`);
        const fs = parseFloat(getComputedStyle(el).fontSize);
        if (arte.classList.contains('ie-arte') && fs < 22) out.push(`fonte ${fs}px < 22: "${el.textContent.trim().slice(0, 30)}"`);
      });
      return out;
    });
    await page.screenshot({ path: path.join(outDir, c + '.png'), fullPage: true });
    await page.close();
    report.push({ c, w, h, errs, issues });
  }
  await browser.close();
  for (const r of report) {
    const bad = r.errs.length || r.issues.length;
    console.log(`${bad ? '!!' : 'ok'} ${r.c} ${r.w}x${r.h}` + (bad ? '\n   ' + [...r.errs, ...r.issues].join('\n   ') : ''));
  }
})();
