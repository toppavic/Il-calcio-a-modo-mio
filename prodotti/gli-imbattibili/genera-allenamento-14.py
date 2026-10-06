"""Genera allenamento-14.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 14
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
                      "la seduta del lunedì della Juniores"))

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


# Corsa sulla metà campo: diagonali in allungo (oro), lati corti di recupero (bianco)
ccvv_svg = f'''<svg class="diagram" viewBox="0 0 500 250" style="width:78mm;margin:0 auto">
    <rect width="500" height="250" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5" stroke-opacity=".6">
      <rect x="40" y="25" width="420" height="200"/>
    </g>
    {freccia("M58,207 L440,43", oro=True)}
    {freccia("M444,46 L444,198", tratteggio=True)}
    {freccia("M440,207 L60,43", oro=True)}
    {freccia("M56,46 L56,196", tratteggio=True)}
    <g font-family="Oswald" font-size="13" fill="#fff" letter-spacing="1">
      <text x="160" y="105" fill="#f2c230">ALLUNGO</text>
      <text x="290" y="175" fill="#f2c230">ALLUNGO</text>
      <text x="410" y="244">RECUPERO</text><text x="20" y="244">RECUPERO</text>
    </g>
  </svg>'''


def campo_meta_portieri(larghezza="150mm"):
    """Partita a meta con i portieri dietro le mete (Allenamento 14): campo orizzontale."""
    def m(x, y):
        return round(40 + (x - 55) * 1.585), round(20 + (y - 170) * 1.3)
    coppie = [(125, 205), (235, 205), (125, 265), (235, 265), (130, 330), (235, 330)]
    gioc = ""
    for x, y in coppie:
        X, Y = m(x, y)
        gioc += g(X - 9, Y, "pB") + g(X + 13, Y + 4, "pA")
    X, Y = m(180, 265); gioc += g(X, Y, "pB")
    X, Y = m(198, 268); gioc += g(X + 8, Y + 4, "pA")
    X, Y = m(190, 228); gioc += g(X, Y, "pJ", "J", "#1d2421")
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:{larghezza};margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <rect x="40" y="20" width="71" height="260" fill="#ffffff" fill-opacity=".14"/>
    <rect x="389" y="20" width="71" height="260" fill="#ffffff" fill-opacity=".14"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="20" width="420" height="260"/>
      <line x1="111" y1="20" x2="111" y2="280"/><line x1="389" y1="20" x2="389" y2="280"/>
    </g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/><rect x="460" y="118" width="10" height="64" fill="#fff"/>
    {g(22, 150, "pP")}{g(478, 150, "pP")}
    <g font-family="Oswald" font-size="14" fill="#fff" letter-spacing="3" text-anchor="middle">
      <text x="75" y="40">META</text><text x="425" y="40">META</text>
    </g>
    {gioc}
  </svg>'''


# ---------- 2. Scheda seduta
scheda = f'''<section class="page">
  <div class="head">
    <div>
      <div class="kicker">In campionato · Seduta del lunedì</div>
      <h2>Allenamento {N}</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">circa 100'</div></div>
    <div><div class="l">Giocatori</div><div class="v">7 contro 7 + jolly · 7 contro 8</div></div>
    <div><div class="l">Campo</div><div class="v">Mete con i portieri e metà campo</div></div>
    <div><div class="l">Focus</div><div class="v">Gioco verticale e difesa in superiorità</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita a meta</div><div class="d">7 contro 7 + jolly · 3 tempi da 12' · 2 tocchi solo verticale, poi 3 tocchi senza compagno di reparto, poi 2 tocchi</div></td><td class="min">40'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Attacco contro difesa</div><div class="d">7 contro 8 · 2 tempi da 15' · tocco libero · chi perde fa 10 flessioni</div></td><td class="min">35'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Corsa con variazioni di velocità</div><div class="d">2 serie da 6' sulla metà campo: lato corto di recupero, diagonale in allungo</div></td><td class="min">12'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:40;background:var(--verde-2)">Partita a meta · 40'</div>
    <div style="flex:35;background:var(--verde)">Attacco-difesa · 35'</div>
    <div style="flex:12;background:var(--oro);color:var(--verde)">CCVV · 12'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il lunedì riparte dalla <b>partita a meta</b>, questa volta con un jolly e con i <b>portieri</b> dietro le mete.
    Poi un <b>attacco contro difesa</b> con la difesa in superiorità numerica (8 contro 7) e una posta in palio:
    chi perde fa le flessioni. Si chiude con la corsa sulla metà campo.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita a meta
meta = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita a meta</h2></div>
  <div class="ex-sub">
    <span class="chip">40 minuti · 3 tempi da 12'</span><span class="chip">7 contro 7 + 1 jolly</span><span class="chip">Un portiere dietro ogni meta</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> la partita a meta degli Allenamenti 12 e 13 con un jolly sempre con chi ha palla. I vincoli cambiano ogni tempo: prima il gioco verticale, poi il passaggio a un altro reparto.</p>
  {campo_meta_portieri("118mm")}
  <div class="three">
    <div class="box"><h4>1° tempo · 12'</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li><li><b>Solo gioco verticale</b>: passaggi in avanti, all'indietro o in diagonale, mai orizzontali</li></ul></div>
    <div class="box"><h4>2° tempo · 12'</h4><ul class="clean"><li>Massimo <b>3 tocchi</b></li><li>Vietato passare al <b>compagno di reparto</b></li></ul></div>
    <div class="box"><h4>3° tempo · 12'</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li></ul></div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Due squadre da 7 e un jolly (J) che gioca con chi ha palla</li>
      <li>Una meta per lato e un portiere dietro ogni meta</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni squadra attacca una meta e, una volta entrata, cerca il gol nella porta difesa dal portiere.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Usare il jolly per creare la superiorità</li>
      <li>Senza compagno di reparto: cercare il giocatore della linea davanti o dietro</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Attacco contro difesa 7 contro 8 + CCVV
def p_(x, y):
    return round(40 + (x - 68) * 1.615), round(22 + (y - 540) * 1.3)


blu = "".join(g(*p_(x, y), "pB") for x, y in
              [(88, 595), (155, 598), (237, 592), (297, 585), (198, 648), (98, 690), (202, 700), (303, 690)])
rossi = "".join(g(*p_(x, y), "pA") for x, y in
                [(205, 610), (172, 683), (238, 688), (105, 730), (165, 730), (232, 730), (295, 718)])
attacco_svg = f'''<svg class="diagram" viewBox="0 0 500 380" style="width:104mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="22" width="420" height="336"/>
      <rect x="205" y="10" width="90" height="12"/><rect x="205" y="358" width="90" height="12"/>
    </g>
    <rect x="40" y="12" width="56" height="10" fill="#f2c230"/><rect x="404" y="12" width="56" height="10" fill="#f2c230"/>
    <g font-family="Oswald" font-size="12" font-weight="700" fill="#f2c230" text-anchor="middle">
      <text x="68" y="38">VS</text><text x="432" y="38">VS</text>
    </g>
    {g(250, 38, "pP")}{g(250, 342, "pP")}
    {blu}{rossi}
    <use href="#palla" x="{p_(165, 730)[0] + 14}" y="{p_(165, 730)[1] + 8}"/>
  </svg>'''

attacco = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Attacco contro difesa · 7 contro 8</h2></div>
  <div class="ex-sub">
    <span class="chip">35 minuti · 2 tempi da 15'</span><span class="chip">7 attaccanti contro 8 difensori</span><span class="chip">Tocco libero</span><span class="chip">10 flessioni</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> la difesa lavora in superiorità numerica e, quando recupera, deve uscire con la palla. L'attacco deve trovare il gol contro una difesa in più.</p>
  <div style="display:flex;gap:5mm;align-items:center">
    <div style="flex:1.15">{attacco_svg}</div>
    <div class="box" style="flex:1"><h4>Regole · 15' per tempo</h4><ul class="clean">
      <li>Tocco libero</li>
      <li>Se l'<b>attacco segna 3 o più gol</b>: la difesa fa <b>10 flessioni</b></li>
      <li>Se la <b>difesa fa gol</b> o <b>porta palla dentro VS</b>: l'attacco fa <b>10 flessioni</b></li>
    </ul></div>
  </div>

  <div class="kicker" style="margin-top:6mm">Esercitazione IV</div>
  <div class="ex-title"><h2 style="font-size:17pt">Corsa con variazioni di velocità · 2 serie da 6'</h2></div>
  <div style="display:flex;gap:6mm;align-items:center;margin-top:3mm">
    <div style="flex:1.1">{ccvv_svg}</div>
    <div class="box" style="flex:1">Come nell'Allenamento 12 ma in <b>2 serie da 6'</b> sulla <b>metà campo</b>:
      <b>lato corto</b> di corsa lenta per recuperare, <b>diagonale</b> in allungo.</div>
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, meta, attacco]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
