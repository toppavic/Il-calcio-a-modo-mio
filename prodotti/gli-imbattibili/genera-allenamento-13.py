"""Genera allenamento-13.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 13
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


def campo_meta(larghezza="104mm"):
    """Campo della partita a meta: 35 m di gioco, una meta di 5 m per lato, 3 porticine dietro ogni meta."""
    porticine = ""
    for i, x in enumerate((170, 250, 330), 1):
        porticine += (f'<rect x="{x-16}" y="14" width="32" height="8" fill="#fff"/>'
                      f'<rect x="{x-16}" y="398" width="32" height="8" fill="#fff"/>'
                      f'<text x="{x}" y="11" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" text-anchor="middle">{i}</text>'
                      f'<text x="{x}" y="418" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" text-anchor="middle">{i}</text>')
    # posizioni come sul foglio: O blu, X rossi
    blu = (g(160, 90, "pB") + g(238, 90, "pB") + g(340, 90, "pB")
           + g(160, 160, "pB") + g(250, 158, "pB") + g(340, 160, "pB") + g(250, 240, "pB"))
    rossi = (g(262, 96, "pA") + g(168, 190, "pA") + g(255, 192, "pA") + g(335, 190, "pA")
             + g(160, 290, "pA") + g(262, 268, "pA") + g(340, 290, "pA"))
    return f'''<svg class="diagram" viewBox="0 0 500 422" style="width:{larghezza};margin:0 auto">
    <rect width="500" height="422" fill="url(#strisce)"/>
    <rect x="130" y="22" width="240" height="42" fill="#ffffff" fill-opacity=".14"/>
    <rect x="130" y="356" width="240" height="42" fill="#ffffff" fill-opacity=".14"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="130" y="22" width="240" height="376"/>
      <line x1="130" y1="64" x2="370" y2="64"/><line x1="130" y1="356" x2="370" y2="356"/>
    </g>
    {porticine}
    <g font-family="Oswald" font-size="14" fill="#fff" letter-spacing="3" text-anchor="middle">
      <text x="250" y="48">META</text><text x="250" y="382">META</text>
    </g>
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="380" y="47">5 M</text><text x="380" y="381">5 M</text>
      <text x="380" y="214">35 M</text>
    </g>
    {blu}{rossi}
    {freccia("M335,178 L310,46", oro=True)}{freccia("M306,40 L322,24", tratteggio=True)}
    <use href="#palla" x="347" y="182"/>
  </svg>'''


# ---------- 2. Scheda seduta
scheda = f'''<section class="page">
  <div class="head">
    <div>
      <div class="kicker">In campionato · Seduta del giovedì</div>
      <h2>Allenamento {N}</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">circa 92'</div></div>
    <div><div class="l">Giocatori</div><div class="v">7 contro 7 · 4 contro 4</div></div>
    <div><div class="l">Campo</div><div class="v">Mete e campo ridotto</div></div>
    <div><div class="l">Focus</div><div class="v">Gioco verticale, rapidità e palle inattive</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita a meta</div><div class="d">3 tempi da 10' · 3 tocchi, poi 2 tocchi e solo gioco verticale, poi 3 tocchi e su ripartenza basta entrare in meta</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Rapidità a stazioni</div><div class="d">3 stazioni · 7 volte per stazione · l'ultima a coppie, partenza da seduti</div></td><td class="min">15'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Calci d'angolo e punizioni offensive</div><div class="d">Lavoro sulle palle inattive a favore</div></td><td class="min">25'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Partita 4 contro 4 + 4 jolly</div><div class="d">4 tempi da 3' · 2 tocchi, sponde a 1 tocco · gol valido solo su sponda e di prima intenzione</div></td><td class="min">12'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita a meta · 30'</div>
    <div style="flex:15;background:var(--oro);color:var(--verde)">Rapidità · 15'</div>
    <div style="flex:25;background:var(--verde)">Palle inattive · 25'</div>
    <div style="flex:12;background:var(--verde-2)">4c4 · 12'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il giovedì riprende la <b>partita a meta</b> del lunedì e la rende più difficile: nel secondo tempo
    si gioca <b>solo in verticale</b>. Poi rapidità, <b>palle inattive offensive</b> in vista della partita
    e per chiudere un 4 contro 4 veloce dove si segna solo di prima sul passaggio della sponda.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita a meta
meta = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita a meta</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 3 tempi da 10'</span><span class="chip">7 contro 7</span><span class="chip">35 m + 2 mete da 5 m</span><span class="chip">3 porticine per lato</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> la stessa partita del lunedì, con un vincolo in più: nel 2° tempo si gioca solo in verticale per arrivare in meta più in fretta.</p>
  <div style="display:flex;gap:6mm;align-items:center">
    <div style="flex:1">{campo_meta("100%")}</div>
    <div style="flex:1;display:flex;flex-direction:column;gap:3mm">
      <div class="box"><h4>1° tempo · 10'</h4><ul class="clean"><li>Massimo <b>3 tocchi</b></li></ul></div>
      <div class="box"><h4>2° tempo · 10'</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li><li><b>Solo gioco verticale</b>: passaggi in avanti, all'indietro o in diagonale, mai orizzontali</li></ul></div>
      <div class="box"><h4>3° tempo · 10'</h4><ul class="clean"><li>Massimo <b>3 tocchi</b></li><li>Su <b>ripartenza</b> (dopo un recupero palla) basta <b>entrare in meta</b>: è gol senza tirare nella porticina</li></ul></div>
    </div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Come nell'Allenamento 12: campo di 35 m con una meta di 5 m per lato</li>
      <li>3 porticine dietro ogni meta</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni squadra attacca una meta. <b>Una volta entrati in meta</b> si fa gol in una delle tre porticine.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Nel gioco verticale smarcarsi in avanti o in diagonale, mai in linea con chi ha palla</li>
      <li>Dopo il recupero attaccare subito la meta</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Rapidità a stazioni + palle inattive
stazioni = [
    ("Scaletta + sprint", "scaletta, poi 10 m di sprint", "7 volte"),
    ("Ostacoli + sprint", "5 m, 3 ostacoli, poi 10 m di sprint", "7 volte"),
    ("Sfida a coppie", "partenza da seduti: vince chi entra per primo nella porticina", "7 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    f'<div class="d">{d}</div></div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Rapidità a stazioni</h2></div>
  <div class="ex-sub">
    <span class="chip">15 minuti</span><span class="chip">3 stazioni</span><span class="chip">7 volte per stazione</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rapidità e reattività. L'ultima stazione diventa una sfida a coppie: si parte da seduti e vince chi arriva per primo.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Una scaletta, 3 ostacoli, una porticina di coni</li>
      <li>10 m di sprint dopo le prime due stazioni</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Si fanno le 7 ripetizioni di una stazione e si passa alla successiva.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Massima velocità in ogni sprint</li>
      <li>Da seduti rialzarsi e partire nello stesso movimento</li>
    </ul></div>
  </div>

  <div class="kicker" style="margin-top:7mm">Esercitazione IV</div>
  <div class="ex-title"><h2 style="font-size:17pt">Calci d'angolo e punizioni offensive · 25'</h2></div>
  <div class="box" style="margin-top:3mm">Lavoro sulle palle inattive a favore in vista della partita. Schemi e posizioni in area: ogni allenatore le organizza come preferisce.</div>
  {footer()}
</section>'''

# ---------- 5. Partita 4 contro 4 + 4 jolly (come l'Allenamento 11)
def campo_sponde():
    dentro = (g(180, 120, "pB") + g(320, 120, "pB") + g(180, 260, "pB") + g(320, 260, "pB")
              + g(200, 150, "pA") + g(300, 150, "pA") + g(200, 230, "pA") + g(300, 230, "pA"))
    sponde_rosse = g(150, 22, "pA") + g(350, 22, "pA") + g(78, 120, "pA") + g(422, 120, "pA")
    sponde_blu = g(150, 358, "pB") + g(350, 358, "pB") + g(78, 260, "pB") + g(422, 260, "pB")
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:112mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="100" y="40" width="300" height="300"/>
      <line x1="100" y1="190" x2="400" y2="190"/>
      <rect x="220" y="28" width="60" height="12"/><rect x="220" y="340" width="60" height="12"/>
    </g>
    {dentro}{sponde_rosse}{sponde_blu}
    {freccia("M212,226 L408,128", tratteggio=True)}{freccia("M412,112 L264,44", tratteggio=True)}
    <use href="#palla" x="214" y="244"/>
    <g font-family="Oswald" font-size="11" fill="#fff" letter-spacing="1">
      <text x="40" y="96">JOLLY</text><text x="436" y="96">JOLLY</text>
    </g>
  </svg>'''


partita = pagina_esercizio(
    "Esercitazione V", "Partita 4 contro 4 + 4 jolly",
    "come nell'Allenamento 11, giocare veloce in spazi stretti usando il compagno fuori dal campo: si segna solo di prima intenzione sul passaggio della sponda.",
    campo_sponde(),
    "<li>4 contro 4 dentro il campo, con due porte piccole</li><li>Ogni squadra ha 4 jolly fuori: due ai lati della porta che attacca e due sulle linee laterali</li>",
    "<p><b>4 tempi da 3 minuti</b>. Si gioca a <b>2 tocchi</b>, le sponde a <b>1 tocco</b>.</p>"
    "<p>Il gol è valido <b>solo su passaggio della sponda e di prima intenzione</b>.</p>",
    "<li>Cercare subito la sponda libera</li><li>Attaccare la porta per calciare di prima quando la palla torna dentro</li>",
    '<span class="chip">12 minuti · 4 tempi da 3\'</span><span class="chip">4 contro 4 + 4 jolly per squadra</span><span class="chip">2 tocchi · sponde 1 tocco</span>')

# ---------- 6. La partita del fine settimana
STAT = [("Tiri in porta", 3, 17), ("Tiri fuori porta", 2, 10), ("Possesso (%)", 50, 50),
        ("Calci d'angolo", 2, 13), ("Fuorigioco", 2, 1), ("Falli", 7, 6),
        ("Cartellini gialli", 2, 0), ("Cartellini rossi", 0, 0), ("Calci di rinvio", 11, 2)]
righe = ""
for lab, a, b in STAT:
    tot = (a + b) or 1
    righe += (f'<tr><td class="v">{a}</td><td><div class="lab">{lab}</div><div class="barra">'
              f'<div style="flex:{a / tot:.3f};background:#c9d3ce"></div>'
              f'<div style="flex:{b / tot:.3f};background:var(--oro)"></div></div></td>'
              f'<td class="v dx">{b}</td></tr>')

risultato = f'''<section class="page">
  <div class="kicker">Il fine settimana</div>
  <div class="ex-title"><h2>La partita</h2></div>
  <p class="obj">Dopo le sedute del lunedì e del giovedì, il risultato della partita.</p>
  <div class="tabellone">
    <div class="sq">
      <div class="nome">Avversari</div>
      <div class="ris">2 – 4</div>
      <div class="nome noi">Gli Imbattibili</div>
    </div>
    <div class="tempi">PRIMO TEMPO 1 – 4 · SECONDO TEMPO 1 – 0</div>
  </div>
  <h3>Statistiche</h3>
  <table class="stat">{righe}</table>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, meta, rapidita, partita, risultato]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
