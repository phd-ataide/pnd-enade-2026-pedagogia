# -*- coding: utf-8 -*-
"""
Monta o app.html final: HTML + CSS + JS + dados (JSON) embutidos, 100% standalone.
"""
import json

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

official = load("official_questions.json")
practice = load("practice_questions.json")
trilha = load("trilha.json")
teoria = load("teoria.json")
dicas = load("dicas.json")
discursiva = load("discursiva_guide.json")

with open("app/style.css", encoding="utf-8") as f:
    css = f.read()
with open("app/app.js", encoding="utf-8") as f:
    js = f.read()

def js_json(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</script", "<\\/script").replace("<!--", "<\\!--")

data_script = (
    "const OFFICIAL = " + js_json(official) + ";\n" +
    "const PRACTICE = " + js_json(practice) + ";\n" +
    "const TRILHA = " + js_json(trilha) + ";\n" +
    "const TEORIA = " + js_json(teoria) + ";\n" +
    "const DICAS = " + js_json(dicas) + ";\n" +
    "const DISCURSIVA = " + js_json(discursiva) + ";\n"
)

NAV_ITEMS = [
    ("inicio", "🏠 Início"),
    ("trilha", "📅 Trilha"),
    ("dicas", "💡 Dicas de Prova"),
    ("teoria", "📚 Teoria"),
    ("simulado", "📝 Simulado Oficial"),
    ("praticar", "🎯 Praticar por Tema"),
    ("banco", "📖 Banco Comentado"),
    ("progresso", "📊 Meu Progresso"),
]

nav_html = "\n".join(
    "<button data-view=\"{v}\"{active}>{label}</button>".format(
        v=v, label=label, active=" class=\"active\"" if v == "inicio" else ""
    )
    for v, label in NAV_ITEMS
)

views_html = "\n".join(
    "<section id=\"view-{v}\" class=\"{hidden}\"></section>".format(
        v=v, hidden="" if v == "inicio" else "hidden"
    )
    for v, _ in NAV_ITEMS
)

html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>PND / ENADE 2026 — Pedagogia UniFECAF — App de Estudos</title>
<meta name="description" content="Aplicativo de estudos para o PND/ENADE 2026 - Pedagogia. Trilha de estudos, banco de questoes comentadas, simulados e dicas de prova.">
<style>
""" + css + """
</style>
</head>
<body>

<div id="topbar">
  <div class="brand">
    <span>🎓 PND/ENADE 2026 · Pedagogia</span>
    <span class="badge">UniFECAF</span>
  </div>
  <div id="countdown-mini">calculando...</div>
</div>

<nav id="mainnav">
""" + nav_html + """
</nav>

<main>
""" + views_html + """
</main>

<footer>
  Aplicativo de estudos independente, elaborado com base na prova real do PND 2025 (Pedagogia).<br>
  Seu progresso é salvo apenas neste navegador (localStorage) — nenhum dado é enviado a servidores.<br>
  UniFECAF · AI First — material de apoio extraoficial, não substitui os comunicados oficiais do INEP.
</footer>

<div id="modal-questao" class="hidden" style="position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:100;display:flex;align-items:center;justify-content:center;padding:1rem;">
  <div style="background:#fff;border-radius:14px;max-width:640px;width:100%;max-height:85vh;overflow-y:auto;padding:1.3rem;position:relative;">
    <button id="modal-fechar" style="position:absolute;top:.8rem;right:.9rem;border:none;background:#f3f4f6;border-radius:50%;width:32px;height:32px;font-size:1rem;">✕</button>
    <div id="modal-questao-body"></div>
  </div>
</div>

<script>
""" + data_script + """
</script>
<script>
""" + js + """
</script>

</body>
</html>
"""

with open("app.html", "w", encoding="utf-8") as f:
    f.write(html)

print("app.html gerado:", len(html), "bytes")
