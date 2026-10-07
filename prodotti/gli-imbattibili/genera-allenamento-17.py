"""Genera allenamento-15.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 17
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
    <div><div class="l">Giocatori</div><div class="v">7 contro 7 · 2 contro 2</div></div>
    <div><div class="l">Campo</div><div class="v">Metà campo larga quanto l'area</div></div>
    <div><div class="l">Focus</div><div class="v">Ricerca del portiere, pressione e rapidità</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Ricerca del portiere · lavoro sulla pressione</div><div class="d">7 contro 7 · 2 tempi · 2 tocchi, niente lancio · 1, 2 o 3 punti · nel 2° tempo senza compagno di reparto</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Rapidità a stazioni</div><div class="d">4 stazioni · 5 volte per stazione · l'ultima a coppie</div></td><td class="min">15'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">2 contro 2 a partita</div><div class="d">Campo 20 × 20 m · si parte sempre dal portiere · chi fa gol resta · 4 serie da 1'30"</div></td><td class="min">6'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Partita libera</div><div class="d">Per chiudere la seduta</div></td><td class="min">–</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Ricerca del portiere · 30'</div>
    <div style="flex:15;background:var(--oro);color:var(--verde)">Rapidità · 15'</div>
    <div style="flex:6;background:var(--verde)">2c2</div>
    <div style="flex:15;background:var(--verde-2)">Partita libera</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il giovedì riprende la <b>ricerca del portiere</b> del lunedì e la rende più ricca: a <b>2 tocchi</b> e con tre
    punteggi diversi, dal passaggio al portiere fino al gol dopo il recupero alto. Nel secondo tempo si aggiunge il
    divieto di passare al compagno di reparto. Poi rapidità, 2 contro 2 e partita libera.
  </div>
  {footer()}
</section>'''

# ---------- 3. Ricerca del portiere
ricerca = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Ricerca del portiere · lavoro sulla pressione</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">7 contro 7</span><span class="chip">Metà campo larga quanto l'area</span><span class="chip">2 tocchi · no lancio</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> rispetto al lunedì i tocchi scendono a 2 e i punti premiano tre cose diverse: trovare il portiere, trovarlo partendo da dietro e segnare dopo il recupero alto.</p>
  {campo_ricerca(larghezza="118mm", etichetta="METÀ CAMPO · LARGHEZZA DELL'AREA")}
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:5mm">
    <div class="box"><h4>1° tempo · 15'</h4><ul class="clean"><li>Massimo <b>2 tocchi</b> · <b>no lancio</b></li>
      <li>Passaggio al portiere: <b>1 punto</b></li>
      <li>Passaggio al portiere <b>dalla metà difensiva</b>: <b>2 punti</b></li>
      <li>Palla recuperata nella <b>metà offensiva</b>: si deve cercare il gol, <b>3 punti</b></li></ul></div>
    <div class="box"><h4>2° tempo · 15'</h4><ul class="clean"><li><b>Stesse regole</b> del 1° tempo</li>
      <li>Vietato passare al <b>compagno di reparto</b> (gli attaccanti possono passarla a chi vogliono)</li></ul></div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Metà campo larga quanto l'area di rigore, divisa in due</li>
      <li>Un portiere bersaglio per lato</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni squadra cerca il portiere del lato che attacca. Dopo un recupero nella metà offensiva non si cerca il portiere ma il gol.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Costruire da dietro per i 2 punti</li>
      <li>Pressione alta per i 3 punti</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Rapidità a stazioni
stazioni = [
    ("Scaletta + scatto", "scaletta, poi 10 m di scatto", "5 volte"),
    ("Skip + scatto", "5 m di skip avanti e indietro, poi scatto", "5 volte"),
    ("Scatto con stop", "5 m di scatto, stop al cono, poi 10 m di scatto", "5 volte"),
    ("Sfida a coppie", "8 m fino ai conetti, poi 5 m: chi passa per primo si ferma", "5 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    f'<div class="d">{d}</div></div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

duecontrodue_svg = f'''<svg class="diagram" viewBox="0 0 500 380" style="width:80mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="110" y="40" width="280" height="300"/>
      <rect x="215" y="28" width="70" height="12"/><rect x="215" y="340" width="70" height="12"/>
    </g>
    {g(250, 54, "pP")}{g(250, 326, "pP")}
    {g(190, 130, "pA")}{g(310, 130, "pA")}{g(200, 250, "pB")}{g(300, 250, "pB")}
    {g(180, 14, "pA")}{g(320, 14, "pA")}{g(180, 366, "pB")}{g(320, 366, "pB")}
    <use href="#palla" x="262" y="318"/>
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="400" y="194">20 M</text><text x="236" y="374">20 M</text>
    </g>
  </svg>'''

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Rapidità a stazioni</h2></div>
  <div class="ex-sub">
    <span class="chip">15 minuti</span><span class="chip">4 stazioni</span><span class="chip">5 volte per stazione</span>
  </div>
  <div class="stazioni" style="grid-template-columns:1fr 1fr">{st_html}</div>

  <div class="kicker" style="margin-top:6mm">Esercitazione IV</div>
  <div class="ex-title"><h2 style="font-size:17pt">2 contro 2 a partita · 4 serie da 1'30"</h2></div>
  <div style="display:flex;gap:6mm;align-items:center;margin-top:3mm">
    <div style="flex:1">{duecontrodue_svg}</div>
    <div class="box" style="flex:1"><ul class="clean">
      <li>Campo <b>20 × 20 m</b> con due porte e i portieri</li>
      <li>Si parte <b>sempre dal portiere</b></li>
      <li><b>Chi fa gol resta</b></li>
      <li>Se la palla esce <b>si cambiano tutti e 4</b> i giocatori</li>
    </ul></div>
  </div>

  <div class="chiave">
    <span class="kicker">Esercitazione V · partita libera</span>
    Partita senza vincoli per chiudere la seduta.
  </div>
  {footer()}
</section>'''

risultato = pagina_partita(
    "Sagginale", "Spartaco Banti Barberino", (1, 5), (1, 2), (0, 3),
    [("Tiri in porta", 2, 13), ("Tiri fuori porta", 3, 5), ("Calci d'angolo", 2, 5), ("Fuorigioco", 1, 4),
     ("Falli", 18, 10), ("Cartellini gialli", 1, 2), ("Cartellini rossi", 2, 0), ("Calci di rinvio", 7, 2)],
    noi="dx")

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, ricerca, rapidita, risultato]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
