"""Compila project/tokens.json em tokens.css no layout de format.md e valida a gramática.
Uso: python3 -I compile_tokens.py <dir-project> <saida.css>
Também imprime um relatório de contraste para os pares de texto declarados abaixo.
"""
import json, re, sys

proj, out = sys.argv[1], sys.argv[2]
t = json.load(open(f"{proj}/tokens.json"))
NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
HEX = re.compile(r"^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
ALIAS = re.compile(r"^\{([A-Za-z0-9][A-Za-z0-9_.-]{0,63})\}$")
LEN = re.compile(r"^(-?\d+(\.\d+)?(px|rem|em|%)?|0)$")
errors, seen = [], set()

themes = [th["id"] for th in t["color"]["themes"]]
colors = t["color"]["tokens"]
cnames = {c["name"] for c in colors}

def check_name(n):
    if not NAME.match(n):
        errors.append(f"nome inválido: {n}")
    if n in seen:
        errors.append(f"nome duplicado: {n}")
    seen.add(n)

def cval(v):
    if HEX.match(v):
        return v.lower()
    m = ALIAS.match(v)
    if m:
        if m.group(1) not in cnames:
            errors.append(f"alias para token inexistente: {v}")
        return f"var(--{m.group(1)})"
    if re.match(r"^(rgb|rgba|hsl|hsla|oklch|oklab|lab|lch|color)\([0-9.,%\s/a-z-]*\)$", v):
        return v
    errors.append(f"valor de cor ilegível: {v}")
    return v

first = {}
per = {th: {} for th in themes}
for c in colors:
    check_name(c["name"])
    if not c.get("usage"):
        errors.append(f"sem usage: {c['name']}")
    v = c["value"]
    if isinstance(v, str):
        first[c["name"]] = cval(v)
    else:
        first[c["name"]] = cval(v.get(themes[0]) or next(iter(v.values())))
        for th in themes[1:]:
            if th in v:
                per[th][c["name"]] = cval(v[th])

lines = ["/* Impulse Elite — generated from tokens.json */",
         ":root, [data-theme=\"%s\"] {" % themes[0]]
lines += [f"  --{k}: {v};" for k, v in first.items()]
lines.append("}")
for th in themes[1:]:
    lines.append('[data-theme="%s"] {' % th)
    lines += [f"  --{k}: {v};" for k, v in per[th].items()]
    lines.append("}")

lines.append(":root {")
for fam, body in t.items():
    if fam in ("name", "version", "meta", "color", "type"):
        continue
    if not isinstance(body, dict) or "tokens" not in body:
        errors.append(f"família fora do formato de lista: {fam}")
        continue
    if len(body["tokens"]) > 60:
        errors.append(f"família {fam} passa de 60 tokens")
    for tok in body["tokens"]:
        check_name(tok["name"])
        if not tok.get("usage"):
            errors.append(f"sem usage: {tok['name']}")
        val = str(tok["value"])
        if fam in ("spacing", "radius") and not LEN.match(val):
            errors.append(f"comprimento inválido {tok['name']}={val}")
        if not re.match(r"^[A-Za-z0-9 #%(),./+_-]{1,200}$", val):
            errors.append(f"valor inválido {tok['name']}={val}")
        lines.append(f"  --{tok['name']}: {val};")
for k, stack in t["type"]["families"].items():
    if re.search(r"[;{}<>\\()]", stack):
        errors.append(f"pilha de fonte inválida {k}")
    lines.append(f"  --font-{k}: {stack};")
lines.append("}")

styles = 0
for g in t["type"]["groups"]:
    fam = g["family"]
    for s in g["styles"]:
        styles += 1
        if not NAME.match(s["name"]):
            errors.append(f"estilo inválido {s['name']}")
        if not LEN.match(str(s["fontSize"])):
            errors.append(f"fontSize inválido {s['name']}")
        decl = [f"font-family: var(--font-{s.get('family', fam)})", f"font-size: {s['fontSize']}"]
        if "lineHeight" in s: decl.append(f"line-height: {s['lineHeight']}")
        if "fontWeight" in s: decl.append(f"font-weight: {s['fontWeight']}")
        if "letterSpacing" in s: decl.append(f"letter-spacing: {s['letterSpacing']}")
        if "fontStyle" in s: decl.append(f"font-style: {s['fontStyle']}")
        lines.append(f".{s['name']} {{ " + "; ".join(decl) + "; }")
if styles > 80:
    errors.append("mais de 80 estilos")

open(out, "w").write("\n".join(lines) + "\n")

# ---------- contraste ----------
def resolve(name, th):
    v = per.get(th, {}).get(name) or first[name]
    seen_r = 0
    while v.startswith("var(--") and seen_r < 16:
        n = v[6:-1]
        v = per.get(th, {}).get(n) or first[n]
        seen_r += 1
    return v

def lum(h):
    h = h.lstrip("#")
    if len(h) == 3: h = "".join(ch * 2 for ch in h)
    r, g, b = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

# (texto, fundo, mínimo, descrição)
PAIRS = [
    ("tinta", "fundo", 4.5, "texto principal"),
    ("tinta", "superficie", 4.5, "texto em cartão"),
    ("tinta", "superficie-alta", 4.5, "texto em balão alto"),
    ("tinta-suave", "fundo", 4.5, "apoio"),
    ("tinta-suave", "superficie", 4.5, "apoio em cartão"),
    ("tinta-suave", "superficie-alta", 4.5, "hora no balão alto"),
    ("destaque", "fundo", 4.5, "destaque"),
    ("destaque", "superficie", 4.5, "destaque em cartão"),
    ("destaque", "superficie-alta", 4.5, "destaque em balão alto"),
    ("on-destaque", "destaque", 4.5, "botão"),
    ("tinta-suave", "placa", 4.5, "apoio sobre placa de vídeo"),
    ("tinta", "placa", 4.5, "texto sobre placa de vídeo"),
    ("filete-forte", "fundo", 3.0, "marca estrutural"),
    ("filete-forte", "superficie", 3.0, "marca estrutural em cartão"),
]
print("CONTRASTE")
for th in themes:
    for a, b, mn, d in PAIRS:
        if a not in first or b not in first:
            continue
        ca, cb = resolve(a, th), resolve(b, th)
        if not (HEX.match(ca) and HEX.match(cb)):
            print(f"  [{th}] {a}/{b}: não-hex, pulado"); continue
        r = ratio(ca, cb)
        flag = "OK " if r >= mn else "FALHA"
        print(f"  {flag} [{th}] {a} {ca} sobre {b} {cb}: {r:.2f} (mín {mn}) {d}")
print("ERROS" if errors else "Sem erros de gramática.")
for e in errors:
    print("  -", e)
