"""Genera allenamento-15.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 19
TESTO_PIEDE = f"In campionato · Allenamento {N}"

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      f"<title>Gli Imbattibili – In campionato, Allenamento {N}</title>")
# stili in più: stazioni (come nell'Allenamento 11) e pagina della partita
testa = testa.replace("</style>\n</head>", """.stazioni { display: grid; grid-template-columns: 1fr; gap: 3mm; margin: 2mm 0 5mm; }
.stazione { display: flex; gap: 4mm; align-items: center; background: #f3f5f2; border-radius: 2mm; padding: 3.5mm 4mm; }
.stazione .n { flex: none; width: 10mm; height: 10mm; border-radius: 50%; background: var(--verde); color: var(--oro); font-family: Oswald, sans-serif; font-weight: 700; font-size: 15pt; display: flex; align-items: center; justify-content: center; }
.stazione .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 12pt; letter-spacing: .02em; line-height: 1.2; }
.stazione .d { font-size: 9.5pt; color: #5d6b65; margin-top: .5mm; }
.stazione .q { margin-left: auto; flex: none; font-family: Oswald, sans-serif; font-size: 13pt; color: var(--verde); font-weight: 700; text-align: right; }
.tabellone { background: var(--verde); color: #fff; border-radius: 3mm; padding: 9mm 8mm 7mm; margin: 6mm 0 7mm; text-align: center; }
.tabellone .sq { display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 6mm; }
.tabellone .nome { font-family: Oswald, sans-serif; text-transform: uppercase; font-size: 15pt; line-height: 1.15; letter-spacing: .02em; }
.tabellone .nome.noi { color: var(--oro); }
.tabellone .ris { font-family: Oswald, sans-serif; font-weight: 700; font-size: 46pt; line-height: 1; }
.tabellone .tempi { margin-top: 4mm; font-size: 10pt; color: #b9cfc4; letter-spacing: .04em; }
.stat { width: 100%; border-collapse: collapse; }
.stat td { padding: 2.2mm 0; font-size: 10pt; vertical-align: middle; }
.stat .v { font-family: Oswald, sans-serif; font-size: 14pt; width: 12mm; color: var(--verde); }
.stat .v.dx { text-align: right; }
.stat .lab { text-align: center; font-size: 9.5pt; color: #5d6b65; padding-bottom: 1mm; }
.stat .barra { display: flex; height: 3mm; gap: 1mm; }
.stat .barra div { border-radius: 1mm; }
</style>
</head>""", 1)
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("precampionato/allenamento-01.jpg", f"campionato/allenamento-{N}.jpg")
             .replace("Precampionato · Allenamento 1", TESTO_PIEDE)
             .replace("la prima seduta della Juniores",
                      "la seduta del giovedì della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>{TESTO_PIEDE}</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def pagina_esercizio(kicker, titolo, obiettivo, schema, org, svol, chiave, chips=""):
    chips_html = f'<div class="ex-sub">{chips}</div>' if chips else ""
    return f'''<section class="page">
  <div class="kicker">{kicker}</div>
  <div class="ex-title"><h2>{titolo}</h2></div>
  {chips_html}
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> {obiettivo}</p>
  {schema}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">{org}</ul></div>
    <div class="box"><h4>Svolgimento</h4>{svol}</div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">{chiave}</ul></div>
  </div>
  {footer()}
</section>'''


def pagina_partita(casa, ospiti, gol, primo, secondo, stat, noi="dx"):
    righe = ""
    for lab, a, b in stat:
        tot = (a + b) or 1
        ca, cb = ("#c9d3ce", "var(--oro)") if noi == "dx" else ("var(--oro)", "#c9d3ce")
        righe += (f'<tr><td class="v">{a}</td><td><div class="lab">{lab}</div><div class="barra">'
                  f'<div style="flex:{a / tot:.3f};background:{ca}"></div>'
                  f'<div style="flex:{b / tot:.3f};background:{cb}"></div></div></td>'
                  f'<td class="v dx">{b}</td></tr>')
    cl_a, cl_b = ("nome", "nome noi") if noi == "dx" else ("nome noi", "nome")
    return f'''<section class="page">
  <div class="kicker">Il fine settimana</div>
  <div class="ex-title"><h2>La partita</h2></div>
  <p class="obj">Dopo le sedute del lunedì e del giovedì, il risultato della partita.</p>
  <div class="tabellone">
    <div class="sq">
      <div class="{cl_a}">{casa}</div>
      <div class="ris">{gol[0]} – {gol[1]}</div>
      <div class="{cl_b}">{ospiti}</div>
    </div>
    <div class="tempi">PRIMO TEMPO {primo[0]} – {primo[1]} · SECONDO TEMPO {secondo[0]} – {secondo[1]}</div>
  </div>
  <h3>Statistiche</h3>
  <table class="stat">{righe}</table>
  {footer()}
</section>'''


# ---------- 2. Scheda seduta
scheda = f'''<section class="page">
  <div class="head">
    <div>
      <div class="kicker">In campionato · Seduta del giovedì</div>
      <h2>Allenamento {N}</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">circa 80'</div></div>
    <div><div class="l">Giocatori</div><div class="v">Due squadre + jolly · 2 contro 2</div></div>
    <div><div class="l">Campo</div><div class="v">Mete con le porte · campo ridotto</div></div>
    <div><div class="l">Focus</div><div class="v">Rapidità e attacco alla meta</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Rapidità a stazioni</div><div class="d">3 sfide a coppie · 5 volte per stazione · chi arriva dopo fa altri 5 m</div></td><td class="min">20'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Partita attacco alla meta</div><div class="d">2 tempi da 15' · 2 tocchi · nel 2° tempo senza compagno di reparto</div></td><td class="min">30'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">2 contro 2 con sponde</div><div class="d">Tocco libero · 4 serie da 1'30" · gol con la sponda doppio</div></td><td class="min">6'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Partita libera</div><div class="d">Per chiudere la seduta</div></td><td class="min">15'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:20;background:var(--oro);color:var(--verde)">Rapidità · 20'</div>
    <div style="flex:30;background:var(--verde-2)">Attacco alla meta · 30'</div>
    <div style="flex:6;background:var(--verde)">2c2</div>
    <div style="flex:15;background:var(--verde-2)">Partita · 15'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Si parte dalla <b>rapidità</b>, tutta a sfide a coppie con partenze diverse. Poi l'<b>attacco alla meta</b>
    con il jolly, che nel secondo tempo diventa più difficile perché non si può passare al compagno di reparto.
    Si chiude con un 2 contro 2 che premia il gioco con le sponde e la partita libera.
  </div>
  {footer()}
</section>'''

# ---------- 3. Rapidità + attacco alla meta
stazioni = [
    ("Partenza da seduti", "a coppie: 10 m fino ai conetti, poi 5 m · chi arriva dopo fa altri 5 m", "5 volte"),
    ("Partenza guardando dietro", "a coppie: 10 m fino ai conetti, poi 5 m · chi arriva dopo fa altri 5 m", "5 volte"),
    ("Partenza con skip alto", "a coppie: 10 m fino ai conetti, poi 5 m", "5 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    f'<div class="d">{d}</div></div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Rapidità a stazioni · sfide a coppie</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti</span><span class="chip">3 stazioni</span><span class="chip">5 volte per stazione</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rapidità e reazione con tre partenze diverse. La sfida a coppie tiene alta l'intensità: chi perde paga con altri 5 metri.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Giocatori a coppie</li><li>Conetti a 10 m e poi a 5 m</li></ul></div>
    <div class="box"><h4>Svolgimento</h4><p>Si fanno le 5 ripetizioni di una stazione e si passa alla successiva.</p></div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Partenza esplosiva qualunque sia la posizione</li><li>Guardando dietro: girarsi e partire in un solo movimento</li></ul></div>
  </div>
  {footer()}
</section>'''

meta_svg = f'''<svg class="diagram" viewBox="0 0 500 300" style="width:132mm;margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <rect x="40" y="20" width="60" height="260" fill="#ffffff" fill-opacity=".14"/>
    <rect x="400" y="20" width="60" height="260" fill="#ffffff" fill-opacity=".14"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="20" width="420" height="260"/>
      <line x1="100" y1="20" x2="100" y2="280"/><line x1="400" y1="20" x2="400" y2="280"/>
    </g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/><rect x="460" y="118" width="10" height="64" fill="#fff"/>
    {g(22, 150, "pP")}{g(478, 150, "pP")}
    <g font-family="Oswald" font-size="13" fill="#fff" letter-spacing="3" text-anchor="middle">
      <text x="70" y="40">META</text><text x="430" y="40">META</text>
    </g>
    {g(150, 70, "pA")}{g(150, 150, "pA")}{g(150, 230, "pA")}{g(230, 110, "pA")}{g(230, 200, "pA")}{g(320, 150, "pA")}{g(370, 80, "pA")}
    {g(350, 70, "pB")}{g(350, 230, "pB")}{g(370, 150, "pB")}{g(270, 110, "pB")}{g(270, 200, "pB")}{g(180, 150, "pB")}{g(130, 220, "pB")}
    {g(250, 155, "pJ", "J", "#1d2421")}
  </svg>'''

attmeta = pagina_esercizio(
    "Esercitazione III", "Partita attacco alla meta",
    "attaccare la meta con un jolly sempre con chi ha palla. Nel 2° tempo il divieto di passare al compagno di reparto obbliga a cercare la linea davanti o dietro.",
    meta_svg,
    "<li>Una meta per lato con la porta e il portiere dietro</li><li>Due squadre e un jolly (J) con chi ha palla</li>",
    "<p><b>1° tempo · 15'</b>: massimo <b>2 tocchi</b>.</p>"
    "<p><b>2° tempo · 15'</b>: massimo <b>2 tocchi</b>, vietato passare al <b>compagno di reparto</b> (gli attaccanti con chi vogliono).</p>",
    "<li>Usare il jolly per creare la superiorità</li><li>Attaccare la meta appena si apre lo spazio</li>",
    '<span class="chip">30 minuti · 2 tempi da 15\'</span><span class="chip">Due squadre + jolly</span><span class="chip">2 tocchi</span>')

# ---------- 4. 2 contro 2 con sponde
duec2_svg = f'''<svg class="diagram" viewBox="0 0 500 300" style="width:92mm;margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5"><rect x="100" y="40" width="300" height="220"/></g>
    <rect x="90" y="120" width="10" height="60" fill="#fff"/><rect x="400" y="120" width="10" height="60" fill="#fff"/>
    {g(112, 150, "pP")}{g(388, 150, "pP")}
    {g(250, 22, "pJ", "J", "#1d2421")}{g(250, 278, "pJ", "J", "#1d2421")}
    {g(190, 100, "pB")}{g(190, 200, "pB")}{g(310, 100, "pA")}{g(310, 200, "pA")}
    {freccia("M300,108 L258,40", tratteggio=True)}{freccia("M258,40 L190,90", tratteggio=True)}
  </svg>'''

duec2 = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>2 contro 2 con sponde</h2></div>
  <div class="ex-sub">
    <span class="chip">4 serie da 1'30"</span><span class="chip">2 contro 2 + 2 sponde</span><span class="chip">Tocco libero</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> duelli a tocco libero usando le due sponde (J) fuori dal campo: il gol dopo la sponda vale doppio.</p>
  <div style="display:flex;gap:6mm;align-items:center">
    <div style="flex:1.2">{duec2_svg}</div>
    <div class="box" style="flex:1"><ul class="clean">
      <li>Due porte con i portieri, due sponde (J) sui lati lunghi</li>
      <li>Tocco libero</li>
      <li><b>Gol dopo la sponda: doppio</b></li>
    </ul></div>
  </div>

  <div class="chiave" style="margin-top:8mm">
    <span class="kicker">Esercitazione V · partita libera · 15'</span>
    Partita senza vincoli per chiudere la seduta.
  </div>
  {footer()}
</section>'''

risultato = pagina_partita(
    "Spartaco Banti Barberino", "Florence", (1, 0), (0, 0), (1, 0),
    [("Tiri in porta", 5, 3), ("Tiri fuori porta", 4, 8), ("Calci d'angolo", 3, 8), ("Fuorigioco", 3, 1),
     ("Falli", 15, 20), ("Cartellini gialli", 4, 3), ("Cartellini rossi", 1, 0), ("Calci di rinvio", 11, 5)],
    noi="sx")

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, rapidita, attmeta, duec2, risultato]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
