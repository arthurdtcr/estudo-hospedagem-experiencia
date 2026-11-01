"""Exporta um roteiro.json para texto legível (formato usado pelos críticos).
Uso: python3 exportar.py <roteiro.json> <saida.md>"""
import json, re, sys, html
def t(s):
    s = html.unescape(s or "")
    s = re.sub(r"</?em>", "*", s); s = re.sub(r"<[^>]+>", "", s)
    return s.strip()
def palavras(*xs):
    return len(" ".join(t(x) for x in xs if x).replace("*", "").split())
d = json.load(open(sys.argv[1]))
o = [f"## Carrossel {d['id']:02d} · {d['titulo']}",
     f"Nível de consciência declarado: {d['nivel']}. Ação pedida: {d['acao']}.", "",
     "Convenção: *itálico* = a única ênfase dourada do slide. \"suave\" = texto de apoio em cinza.", ""]
for i, s in enumerate(d["slides"], 1):
    tp = s["tipo"]; partes = []; txt = []
    if s.get("rotulo"): partes.append(f"rótulo {s['rotulo'].upper()}"); txt.append(s["rotulo"])
    if tp == "capa":
        partes.append(f"\"{t(s['texto'])}\"" + (f" · menor: \"{t(s['sub'])}\"" if s.get("sub") else "") + " · Arraste"); txt += [s["texto"], s.get("sub")]
    elif tp == "pausa":
        partes.append(" / ".join(f"\"{t(l)}\"" for l in s["linhas"])); txt += s["linhas"]
    elif tp == "texto":
        for k, v in s["blocos"]:
            if k == "filete": partes.append("(filete)")
            else: partes.append(f"{k} \"{t(v)}\""); txt.append(v)
    elif tp == "numeral":
        for k in ("numeral", "lead", "corpo", "nota"):
            if s.get(k): partes.append(f"{k} \"{t(s[k])}\""); txt.append(s[k])
    elif tp == "lista":
        if s.get("inicio"): partes.append(f"(numeração começa em {s['inicio']})")
        partes.append("itens: " + "; ".join(f"{t(a)}: {t(b)}" if b else t(a) for a, b in s["itens"]))
        for a, b in s["itens"]: txt += [a, b]
        if s.get("fecho"): partes.append(f"fecho \"{t(s['fecho'])}\""); txt.append(s["fecho"])
    elif tp == "duplo":
        for b in s["blocos"]:
            partes.append(f"{t(b['titulo'])}: " + "; ".join(t(x) for x in b["itens"])); txt += [b["titulo"]] + b["itens"]
    elif tp == "retrato":
        for k in ("foto", "nome", "cargo", "corpo_suave", "corpo"):
            if s.get(k): partes.append(f"{k} \"{t(s[k])}\""); txt.append(s[k]) if k != "foto" else None
    elif tp == "cta":
        for k in ("rotulo2", "manchete", "titulo2", "lead", "chave"):
            if s.get(k): partes.append(f"{k} \"{t(s[k])}\""); txt.append(s[k])
    extra = ", fundo claro" if tp == "pausa" else ""
    o.append(f"{i}. **{s['titulo']}** ({tp}{extra}, {palavras(*txt)} palavras) · " + " · ".join(partes))
o += ["", "Legenda (publicada no perfil, em primeira pessoa do Arthur):", ""]
o += ["> " + l if l else ">" for l in d["legenda"].split("\n")]
open(sys.argv[2], "w").write("\n".join(o) + "\n")
