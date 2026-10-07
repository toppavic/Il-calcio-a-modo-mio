"""Genera allenamento-15.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 16
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


def campo_ricerca(jolly=False, larghezza="150mm", etichetta=""):
    """Ricerca del portiere: campo orizzontale diviso in due metà, un portiere bersaglio per lato."""
    rossi = [(95, 70), (95, 150), (95, 230), (175, 110), (175, 190), (300, 150), (390, 100)]
    blu = [(405, 70), (405, 150), (405, 230), (325, 110), (325, 190), (200, 150), (110, 110)]
    gioc = "".join(g(x, y, "pA") for x, y in rossi) + "".join(g(x, y, "pB") for x, y in blu)
    if jolly:
        gioc += g(250, 230, "pJ", "J", "#1d2421")
    lab = (f'<text x="250" y="292" font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" '
           f'letter-spacing="1">{etichetta}</text>') if etichetta else ""
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:{larghezza};margin:0 auto">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="20" width="420" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/>
    </g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/><rect x="460" y="118" width="10" height="64" fill="#fff"/>
    {g(22, 150, "pP")}{g(478, 150, "pP")}
    {gioc}
    <use href="#palla" x="{300 + 14}" y="{150 + 8}"/>
    {freccia("M312,146 L462,150", tratteggio=True)}
    {lab}
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
    <div><div class="l">Durata</div><div class="v">circa 85'</div></div>
    <div><div class="l">Giocatori</div><div class="v">7 contro 7 + jolly · due squadre</div></div>
    <div><div class="l">Campo</div><div class="v">Due metà con portieri bersaglio</div></div>
    <div><div class="l">Focus</div><div class="v">Ricerca del portiere e pressione</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Ricerca del portiere · lavoro sulla pressione</div><div class="d">7 contro 7 + jolly · 2 tempi da 15' · 3 tocchi, niente lancio · gol dopo il recupero nella metà offensiva = 5 punti · nel 2° tempo solo verticale</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Attacco contro difesa</div><div class="d">2 tempi · tocco libero · la squadra A difende e riparte verso le porticine o la porta</div></td><td class="min">30'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Navette</div><div class="d">5' di 20"-20" sui 100 m · 5' di 15"-15" sugli 80 m · 5' di 10"-10" sui 16 m</div></td><td class="min">15'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Ricerca del portiere · 30'</div>
    <div style="flex:30;background:var(--verde)">Attacco-difesa · 30'</div>
    <div style="flex:15;background:var(--oro);color:var(--verde)">Navette · 15'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Torna la <b>ricerca del portiere</b> del precampionato, ma ora diventa un lavoro sulla <b>pressione</b>:
    niente lanci e un premio grosso (5 punti) per chi recupera palla nella metà offensiva e segna.
    Poi un <b>attacco contro difesa</b> dove chi difende deve anche ripartire e per finire le navette.
  </div>
  {footer()}
</section>'''

# ---------- 3. Ricerca del portiere
ricerca = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Ricerca del portiere · lavoro sulla pressione</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">7 contro 7 + 1 jolly</span><span class="chip">3 tocchi</span><span class="chip">No lancio</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> la ricerca del portiere del precampionato diventa un lavoro sulla pressione. Senza lanci si deve arrivare al portiere palla a terra e il recupero alto vale molto di più.</p>
  {campo_ricerca(jolly=True, larghezza="118mm")}
  <div class="two" style="display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:5mm">
    <div class="box"><h4>1° tempo · 15'</h4><ul class="clean"><li>Massimo <b>3 tocchi</b></li><li><b>No lancio</b></li>
      <li>Se si <b>recupera palla nella metà offensiva</b> si può fare gol: vale <b>5 punti</b></li></ul></div>
    <div class="box"><h4>2° tempo · 15'</h4><ul class="clean"><li>Massimo <b>3 tocchi</b></li><li><b>Solo gioco verticale</b>, <b>no lancio</b></li>
      <li>Se si <b>recupera palla nella metà offensiva</b> si può fare gol: vale <b>5 punti</b></li></ul></div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo diviso in due metà, un portiere bersaglio per lato</li>
      <li>Due squadre da 7 e un jolly (J) con chi ha palla</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni squadra cerca di far arrivare la palla al portiere del lato che attacca. Il gol si può fare solo dopo un recupero nella metà offensiva.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Pressione immediata quando si perde palla</li>
      <li>Dopo il recupero alto attaccare subito la porta</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Attacco contro difesa + navette
attacco_svg = f'''<svg class="diagram" viewBox="0 0 500 380" style="width:100mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="22" width="420" height="336"/>
      <line x1="40" y1="190" x2="460" y2="190"/>
      <rect x="205" y="10" width="90" height="12"/><rect x="205" y="358" width="90" height="12"/>
    </g>
    <rect x="40" y="10" width="56" height="12" fill="#f2c230"/><rect x="404" y="10" width="56" height="12" fill="#f2c230"/>
    <g font-family="Oswald" font-size="12" font-weight="700" fill="#f2c230" text-anchor="middle">
      <text x="68" y="40">1</text><text x="432" y="40">2</text>
    </g>
    {g(250, 38, "pP")}{g(250, 342, "pP")}
    {g(170, 80, "pB")}{g(250, 75, "pB")}{g(330, 80, "pB")}{g(200, 140, "pB")}{g(300, 140, "pB")}
    {g(190, 225, "pA")}{g(250, 222, "pA")}{g(310, 225, "pA")}{g(90, 262, "pA")}{g(410, 262, "pA")}
    {g(150, 300, "pA")}{g(250, 300, "pA")}{g(350, 300, "pA")}
    <g font-family="Oswald" font-size="13" fill="#fff" letter-spacing="2" text-anchor="middle">
      <text x="250" y="178">SQUADRA B</text><text x="250" y="210">SQUADRA A</text>
    </g>
    {freccia("M100,250 L88,46", oro=True)}
  </svg>'''

attacco = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Attacco contro difesa</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi</span><span class="chip">Tocco libero</span><span class="chip">Stesse regole nei due tempi</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> come nell'Allenamento 14, chi difende non deve solo recuperare palla ma anche uscire bene: verso le porticine laterali o verso la porta.</p>
  <div style="display:flex;gap:5mm;align-items:center">
    <div style="flex:1.1">{attacco_svg}</div>
    <div style="flex:1;display:flex;flex-direction:column;gap:3mm">
      <div class="box"><h4>Squadra A · difende</h4><ul class="clean">
        <li>Recuperata la palla deve uscire nella <b>porticina 1 o 2</b>: <b>1 punto</b></li>
        <li>Oppure <b>fare gol</b>: <b>1 punto</b></li></ul></div>
      <div class="box"><h4>Squadra B · attacca</h4><ul class="clean"><li>Deve <b>fare gol</b></li></ul></div>
    </div>
  </div>

  <div class="kicker" style="margin-top:6mm">Esercitazione IV</div>
  <div class="ex-title"><h2 style="font-size:17pt">Navette · 15'</h2></div>
  <table class="intervalli" style="width:100%;border-collapse:collapse;margin-top:2mm">
    <tr><td style="font-family:Oswald;font-size:15pt;color:var(--verde);width:14mm;padding:2.5mm 2mm;border-bottom:1px solid #e3e8e5">5'</td><td style="padding:2.5mm 2mm;border-bottom:1px solid #e3e8e5">20" di corsa e 20" di recupero · navette sui <b>100 m</b></td></tr>
    <tr><td style="font-family:Oswald;font-size:15pt;color:var(--verde);padding:2.5mm 2mm;border-bottom:1px solid #e3e8e5">5'</td><td style="padding:2.5mm 2mm;border-bottom:1px solid #e3e8e5">15" di corsa e 15" di recupero · navette sugli <b>80 m</b></td></tr>
    <tr><td style="font-family:Oswald;font-size:15pt;color:var(--verde);padding:2.5mm 2mm;border-bottom:1px solid #e3e8e5">5'</td><td style="padding:2.5mm 2mm;border-bottom:1px solid #e3e8e5">10" di corsa e 10" di recupero · navette sui <b>16 m</b> (dal fondo campo al limite dell'area)</td></tr>
  </table>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, ricerca, attacco]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
