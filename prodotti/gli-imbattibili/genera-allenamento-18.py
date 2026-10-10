"""Genera allenamento-15.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 18
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


def porta_lettera(x, y, lettera):
    return (f'<rect x="{x-5}" y="{y-16}" width="10" height="32" fill="#f2c230"/>'
            f'<text x="{x+12}" y="{y+5}" font-family="Oswald" font-size="13" font-weight="700" fill="#f2c230">{lettera}</text>')


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
    <div><div class="l">Giocatori</div><div class="v">Due squadre</div></div>
    <div><div class="l">Campo</div><div class="v">3/4 di campo, tutta la larghezza</div></div>
    <div><div class="l">Focus</div><div class="v">Gioco sulla punta e uscita dalla difesa</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita a meta con ricerca della punta</div><div class="d">2 tempi da 15' · 2 tocchi · la squadra B cerca la punta in meta, scarico e filtrante attraverso le porte A, B, C · la squadra A deve fare gol</div></td><td class="min">35'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Attacco contro difesa</div><div class="d">2 tempi da 15' · chi attacca cerca il gol, chi difende esce dalle porticine A, B, C · chi perde fa 10 flessioni</div></td><td class="min">35'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Corsa con variazioni di velocità</div><div class="d">2 ripetute da 8'</div></td><td class="min">20'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:35;background:var(--verde-2)">Meta e punta · 35'</div>
    <div style="flex:35;background:var(--verde)">Attacco-difesa · 35'</div>
    <div style="flex:20;background:var(--oro);color:var(--verde)">CCVV · 20'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Una seduta sul <b>gioco in verticale con la punta</b>: trovarla in meta, giocare sul suo scarico e lanciare
    il compagno in profondità con la filtrante. Poi l'<b>attacco contro difesa</b>, dove chi difende deve anche
    uscire palla al piede dalle porticine, e la corsa con variazioni di velocità.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita a meta con ricerca della punta
meta_svg = f'''<svg class="diagram" viewBox="0 0 500 300" style="width:132mm;margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <rect x="405" y="20" width="55" height="260" fill="#ffffff" fill-opacity=".14"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="20" width="420" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/><line x1="405" y1="20" x2="405" y2="280"/>
    </g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/>{g(22, 150, "pP")}
    {porta_lettera(460, 60, "C")}{porta_lettera(460, 150, "B")}{porta_lettera(460, 240, "A")}
    <g font-family="Oswald" font-size="13" fill="#fff" letter-spacing="3" text-anchor="middle">
      <text x="432" y="40">META</text>
      <text x="145" y="273" font-size="11" letter-spacing="1">← ROSSI (A) ATTACCANO</text><text x="325" y="273" font-size="11" letter-spacing="1">BLU (B) ATTACCANO →</text>
    </g>
    {g(110, 90, "pA")}{g(110, 210, "pA")}{g(185, 150, "pA")}{g(300, 70, "pA")}{g(300, 230, "pA")}
    {g(150, 120, "pB")}{g(200, 230, "pB")}{g(285, 150, "pB")}{g(350, 100, "pB")}{g(360, 210, "pB")}
    {g(432, 150, "pB", "9")}
    {freccia("M297,146 L418,150", tratteggio=True)}
    {freccia("M425,160 L372,204", tratteggio=True)}
    {freccia("M372,214 L455,236", tratteggio=True)}
    {freccia("M352,112 L452,232", oro=True)}
    <use href="#palla" x="297" y="160"/>
  </svg>'''

meta = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita a meta con ricerca della punta</h2></div>
  <div class="ex-sub">
    <span class="chip">35 minuti · 2 tempi da 15'</span><span class="chip">3/4 di campo · tutta la larghezza</span><span class="chip">2 tocchi</span><span class="chip">Porte A, B, C</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> giocare sulla punta: trovarla in zona meta, sfruttare il suo scarico e mandare un compagno in profondità con la filtrante.</p>
  {meta_svg}
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:5mm">
    <div class="box"><h4>Squadra B · ricerca della punta</h4><ul class="clean">
      <li>Deve cercare l'<b>attaccante in zona meta</b></li>
      <li>Con il suo <b>scarico</b> l'attaccante deve permettere una <b>filtrante</b> per un compagno</li>
      <li>Il compagno deve <b>attraversare una delle porte A, B, C</b></li></ul></div>
    <div class="box"><h4>Squadra A · gol</h4><ul class="clean">
      <li>Deve <b>fare gol</b> nella porta con il portiere</li>
      <li>Se recupera palla nella <b>metà offensiva</b>, il gol vale <b>doppio</b></li></ul></div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>3/4 di campo, tutta la larghezza</li>
      <li>Da un lato una porta con il portiere, dall'altro la zona meta con le porte A, B, C</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si gioca a <b>2 tocchi</b>. Le due squadre hanno obiettivi diversi (vedi riquadri sopra).</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>La punta riceve e scarica subito</li>
      <li>Chi riceve lo scarico ha già visto il compagno che attacca la profondità</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Attacco contro difesa + CCVV
attacco_svg = f'''<svg class="diagram" viewBox="0 0 500 300" style="width:118mm;margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5"><rect x="40" y="20" width="420" height="260"/></g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/>{g(22, 150, "pP")}
    {porta_lettera(460, 60, "C")}{porta_lettera(460, 150, "B")}{porta_lettera(460, 240, "A")}
    {g(80, 80, "pB")}{g(80, 130, "pB")}{g(80, 175, "pB")}{g(80, 220, "pB")}{g(150, 110, "pB")}{g(150, 195, "pB")}{g(260, 150, "pB")}
    {g(120, 95, "pA")}{g(120, 160, "pA")}{g(120, 230, "pA")}{g(200, 130, "pA")}{g(200, 200, "pA")}{g(300, 120, "pA")}{g(320, 180, "pA")}
    {freccia("M268,146 L448,152", oro=True)}
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="60" y="272">BLU: DIFENDONO LA PORTA, RECUPERANO ED ESCONO DALLE PORTICINE</text>
    </g>
  </svg>'''

attacco = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Attacco contro difesa</h2></div>
  <div class="ex-sub">
    <span class="chip">35 minuti · 2 tempi da 15'</span><span class="chip">Porticine A, B, C</span><span class="chip">10 flessioni</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> come negli Allenamenti 14 e 16 chi difende, dopo il recupero, deve uscire palla al piede. Questa volta le porticine sono tre.</p>
  {attacco_svg}
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:5mm">
    <div class="box"><h4>Regole</h4><ul class="clean">
      <li><b>Chi attacca la porta</b> deve fare gol e difendere le porticine</li>
      <li><b>Chi difende la porta</b> deve attraversare con la palla le porticine A, B o C</li></ul></div>
    <div class="box"><h4>Chi vince</h4><ul class="clean">
      <li>L'attacco vince se segna <b>3 o più gol</b> (ogni gol oltre il terzo: <b>1 flessione in più</b> per chi perde)</li>
      <li>Chi perde fa <b>10 flessioni</b></li></ul></div>
  </div>

  <div class="kicker" style="margin-top:7mm">Esercitazione IV</div>
  <div class="ex-title"><h2 style="font-size:17pt">Corsa con variazioni di velocità · 2 ripetute da 8'</h2></div>
  <div class="box" style="margin-top:3mm">Due ripetute da 8 minuti di corsa con variazioni di velocità (20' in tutto con il recupero).</div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, meta, attacco]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
