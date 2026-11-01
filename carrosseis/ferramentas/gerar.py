"""Gera UM slide (ou o canvas.json) de um carrossel a partir de roteiros-finais.json.

Uso:
  python3 gerar.py <json> <carrossel_id> canvas <root>
  python3 gerar.py <json> <carrossel_id> <n_slide> <root>
"""
import json, sys, os, datetime

DS_URL = "https://claude.ai/artifact/9eggYVve7p8i6mN5X71wRe"
DS_VERSION = "1793507287-6e32"

HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="estilo/tokens.css">
<link rel="stylesheet" href="ds/impulse-elite/components/bundle.css">
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Montserrat:wght@400;500;600&amp;display=swap">
<style>
{style}
</style>
</helmet>
"""
STYLE_NOITE = "body{margin:0;background:#000000}\na{color:#E0BE72}a:hover{color:#FBEE9A}"
STYLE_MARFIM = "body{margin:0;background:#F4F1E9}\na{color:#7A5E1B}a:hover{color:#000000}"
TAIL = """</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1350}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
"""
ROOT_ATTRS = 'style="width: 1080px; height: 1350px; font-family: var(--font-sans); color: var(--tinta)"'


def nome_arquivo(n):
    return "Main.dc.html" if n == 1 else "Slide%02d.dc.html" % n


def bloco(tipo, html):
    if tipo == "manchete":
        return '      <h2 class="manchete ie-serif">%s</h2>' % html
    if tipo == "titulo":
        return '      <p class="titulo ie-serif">%s</p>' % html
    if tipo == "lead":
        return '      <p class="lead ie-sans ie-largura">%s</p>' % html
    if tipo == "corpo":
        return '      <p class="corpo ie-sans ie-largura">%s</p>' % html
    if tipo == "corpo-suave":
        return '      <p class="corpo ie-sans ie-suave ie-largura">%s</p>' % html
    if tipo == "nota":
        return '      <p class="nota ie-sans ie-suave ie-largura">%s</p>' % html
    if tipo == "filete":
        return '      <div class="ie-filete" style="max-width: 820px"></div>'
    raise ValueError(tipo)


def corpo_slide(s):
    t = s["tipo"]
    if t == "capa":
        return f"""<div class="ie-arte ie-grao ie-brilho" {ROOT_ATTRS}>
  <span class="ie-diagonal" style="left: 900px; top: -80px; height: 700px"></span>
  <div class="ie-area ie-base">
    <h1 class="capa ie-serif">{s['texto']}</h1>
    <div style="display: flex; align-items: center; gap: 24px; margin-top: 96px">
      <div class="ie-filete ie-ouro-linha" style="width: 56px"></div>
      <span class="nota ie-sans ie-suave ie-maiusc" style="letter-spacing: 0.32em">Arraste</span>
    </div>
  </div>
</div>
""", STYLE_NOITE
    if t == "pausa":
        linhas = []
        for i, l in enumerate(s["linhas"]):
            extra = ' style="margin-top: 72px"' if i == len(s["linhas"]) - 1 and len(s["linhas"]) > 2 else ''
            linhas.append(f'    <p class="manchete ie-serif"{extra}>{l}</p>')
        return f"""<div class="ie-arte" data-theme="marfim" {ROOT_ATTRS}>
  <div class="ie-area ie-centro" style="gap: 24px">
""" + "\n".join(linhas) + """
  </div>
</div>
""", STYLE_MARFIM
    if t == "texto":
        blocos = "\n".join(bloco(k, v) for k, v in s["blocos"])
        return f"""<div class="ie-arte ie-grao" {ROOT_ATTRS}>
  <div class="ie-area ie-entre">
    <div class="ie-rotulo rotulo">{s['rotulo']}</div>
    <div style="display: flex; flex-direction: column; gap: 48px">
{blocos}
    </div>
  </div>
</div>
""", STYLE_NOITE
    if t == "numeral":
        extra = ""
        if s.get("corpo"):
            extra = "\n" + bloco("corpo", s["corpo"])
        return f"""<div class="ie-arte ie-grao" {ROOT_ATTRS}>
  <div class="ie-area ie-entre">
    <div class="ie-rotulo rotulo">{s['rotulo']}</div>
    <div style="display: flex; flex-direction: column; gap: 40px">
      <div class="numeral ie-serif metal-text">{s['numeral']}</div>
      <p class="lead ie-sans ie-largura">{s['lead']}</p>
      <div class="ie-filete" style="max-width: 820px"></div>
      <p class="nota ie-sans ie-suave ie-largura">{s['nota']}</p>{extra}
    </div>
  </div>
</div>
""", STYLE_NOITE
    if t == "lista":
        itens = "\n".join(
            f'      <li><div><p class="item ie-serif">{a}</p><p class="corpo ie-sans ie-suave">{b}</p></div></li>'
            for a, b in s["itens"])
        fecho = f'\n    <p class="titulo ie-serif">{s["fecho"]}</p>' if s.get("fecho") else ''
        ini = f' style="counter-reset: ie {s["inicio"]-1}"' if s.get("inicio") else ''
        return f"""<div class="ie-arte ie-grao" {ROOT_ATTRS}>
  <div class="ie-area ie-entre">
    <div class="ie-rotulo rotulo">{s['rotulo']}</div>
    <ol class="ie-lista"{ini}>
{itens}
    </ol>{fecho}
  </div>
</div>
""", STYLE_NOITE
    if t == "duplo":
        cols = []
        for b in s["blocos"]:
            itens = "\n".join(f'        <p class="corpo ie-sans ie-suave">{x}</p>' for x in b["itens"])
            cols.append(f"""      <div style="display: flex; flex-direction: column; gap: 24px; padding-top: 48px; border-top: 1.5px solid var(--filete)">
        <p class="item ie-serif">{b['titulo']}</p>
{itens}
      </div>""")
        return f"""<div class="ie-arte ie-grao" {ROOT_ATTRS}>
  <div class="ie-area ie-entre">
    <div class="ie-rotulo rotulo">{s['rotulo']}</div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 56px">
""" + "\n".join(cols) + """
    </div>
  </div>
</div>
""", STYLE_NOITE
    if t == "retrato":
        return f"""<div class="ie-arte ie-grao" {ROOT_ATTRS}>
  <div class="ie-retrato" style="position: absolute; top: 0; right: 0; width: 1080px; height: 820px; clip-path: none">
    <div class="ie-retrato-vazio">{s['foto']}</div>
  </div>
  <div class="ie-area ie-base" style="gap: 32px">
    <h2 class="titulo ie-serif">{s['nome']}</h2>
    <p class="nota ie-sans ie-ouro ie-maiusc" style="letter-spacing: 0.32em; font-weight: 600">{s['cargo']}</p>
    <div class="ie-filete" style="max-width: 820px; margin-top: 8px"></div>
    <p class="corpo ie-sans ie-suave ie-largura">{s['corpo_suave']}</p>
    <p class="corpo ie-sans ie-largura">{s['corpo']}</p>
  </div>
</div>
""", STYLE_NOITE
    if t == "cta":
        return f"""<div class="ie-arte ie-grao ie-brilho" {ROOT_ATTRS}>
  <span class="ie-diagonal" style="left: 1010px; top: -100px; height: 540px"></span>
  <div class="ie-area ie-entre">
    <div class="ie-rotulo rotulo">Próximo passo</div>
    <div style="display: flex; flex-direction: column; gap: 48px">
      <h2 class="manchete ie-serif">{s['manchete']}</h2>
      <p class="titulo ie-serif">{s['titulo2']}</p>
      <p class="lead ie-sans ie-suave ie-largura">{s['lead']}</p>
      <div><span class="ie-chave"><span>{s['chave']}</span></span></div>
    </div>
  </div>
</div>
""", STYLE_NOITE
    raise ValueError(t)


def slide_html(c, n):
    s = c["slides"][n - 1]
    body, style = corpo_slide(s)
    title = "Slide %d · %s" % (n, s["titulo"])
    return HEAD.format(title=title, style=style) + body + TAIL


def canvas_json(c, now):
    boards, order = {}, []
    for i, s in enumerate(c["slides"], 1):
        f = nome_arquivo(i)
        boards[f] = {"x": (i - 1) * 1160, "y": 0, "w": 1080, "h": 1350, "title": "%d · %s" % (i, s["titulo"])}
        order.append(f)
    total_w = len(c["slides"]) * 1160 - 80
    return {
        "v": 3,
        "createdOnFiles": {"v": 1, "at": now},
        "title": "Carrossel %02d · %s" % (c["id"], c["titulo"].rstrip(".")),
        "launch": {"view": "canvas"},
        "pages": [],
        "boards": boards,
        "order": order,
        "notes": {"titulo": {"x": 0, "y": -300, "text": "Série 2 · Carrossel %d · %s · Impulse Elite · 1080 × 1350" % (c["id"], c["titulo"]), "kind": "title1", "maxW": total_w}},
        "designSystems": [{"title": "Impulse Elite", "namespace": "impulse-elite", "artifact": DS_URL, "version": DS_VERSION, "copiedAt": now}],
    }


if __name__ == "__main__":
    src, cid, what, root = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
    data = {c["id"]: c for c in json.load(open(src))}
    c = data[cid]
    os.makedirs(os.path.join(root, "project"), exist_ok=True)
    if what == "canvas":
        now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        out = os.path.join(root, "project", "canvas.json")
        json.dump(canvas_json(c, now), open(out, "w"), ensure_ascii=False, indent=2)
    else:
        n = int(what)
        out = os.path.join(root, "project", nome_arquivo(n))
        open(out, "w").write(slide_html(c, n))
    print(out)
