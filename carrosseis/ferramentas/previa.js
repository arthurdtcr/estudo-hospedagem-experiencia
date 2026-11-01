const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const root = process.argv[2], out = process.argv[3];
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const c of fs.readdirSync(root).sort()) {
    const proj = path.join(root, c, 'project');
    const order = JSON.parse(fs.readFileSync(path.join(proj, 'canvas.json'))).order;
    for (let i = 0; i < order.length; i++) {
      await page.goto('file://' + path.resolve(proj, order[i]), { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.waitForTimeout(300);
      await page.screenshot({ path: path.join(out, `${c}-${String(i + 1).padStart(2, '0')}.png`), clip: { x: 0, y: 0, width: 1080, height: 1350 } });
    }
  }
  await browser.close();
})();
