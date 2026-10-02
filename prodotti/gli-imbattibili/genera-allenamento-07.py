"""Genera allenamento-07.html partendo dallo stile dell'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 7</title>")
testa = testa.replace("</style>\n</head>", """.stazioni { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; margin: 2mm 0 5mm; }
.stazione { display: flex; gap: 4mm; align-items: center; background: #f3f5f2; border-radius: 2mm; padding: 3.5mm 4mm; }
.stazione .n { flex: none; width: 10mm; height: 10mm; border-radius: 50%; background: var(--verde); color: var(--oro); font-family: Oswald, sans-serif; font-weight: 700; font-size: 15pt; display: flex; align-items: center; justify-content: center; }
.stazione .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 12pt; letter-spacing: .02em; line-height: 1.2; }
.stazione .d { font-size: 9.5pt; color: #5d6b65; margin-top: .5mm; }
.stazione .q { margin-left: auto; flex: none; font-family: Oswald, sans-serif; font-size: 13pt; color: var(--verde); font-weight: 700; text-align: right; }
.intervalli { width: 100%; border-collapse: collapse; margin: 1mm 0 5mm; }
.intervalli td { padding: 3mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 10pt; vertical-align: middle; }
.intervalli .min { font-family: Oswald, sans-serif; font-size: 15pt; color: var(--verde); width: 14mm; }
.intervalli tr.rec td { background: #f3f5f2; color: #5d6b65; padding: 1.5mm 2mm; }
.intervalli tr.rec .min, .intervalli tr.rec .rit { font-size: 11pt; color: #7aa995; }
.intervalli .rit { font-family: Oswald, sans-serif; font-size: 13pt; color: #9a7410; width: 26mm; }
</style>
</head>""", 1)
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("allenamento-01.jpg", "allenamento-07.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 7")
             .replace("la prima seduta della Juniores", "la settima seduta della Juniores"))

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 7</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def mezzo_campo(contenuto, larghezza="150mm"):
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:{larghezza};margin:0 auto">
      <rect width="500" height="380" fill="url(#strisce)"/>
      <g fill="none" stroke="#fff" stroke-width="2.5">
        <rect x="10" y="10" width="480" height="360"/>
        <rect x="103" y="10" width="294" height="110"/><rect x="186" y="10" width="128" height="38"/>
        <path d="M205,120 A55,55 0 0 0 295,120"/>
      </g>
      <rect x="216" y="2" width="68" height="8" fill="#fff"/>
      {g(250, 32, "pP")}
      {contenuto}
    </svg>'''


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


# ---------- 2. Scheda seduta
scheda = f'''<section class="page">
  <div class="head">
    <div>
      <div class="kicker">Precampionato · Settimana 2</div>
      <h2>Allenamento 7</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">100'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">3/4 di campo</div></div>
    <div><div class="l">Focus</div><div class="v">Cambio di ritmo e rapidità</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione e lavoro in cerchio sulle combinazioni di passaggi</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “cambio di ritmo”</div><div class="d">Tocchi diversi tra metà difensiva e metà offensiva · gol valido solo se tutti sono nella metà offensiva · 2 tempi da 15'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Rapidità</div><div class="d">Circuito a 4 stazioni: slalom, skip, scaletta, partenze da seduti</div></td><td class="min">20'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Attacco contro difesa</div><div class="d">9 contro 9 + portiere · 2 tempi da 10'</div></td><td class="min">20'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Punizioni difensive e stretching</div><div class="d">Lavoro sulle punizioni a sfavore, poi stretching finale</div></td><td class="min">20'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:20;background:var(--oro);color:var(--verde)">Rapidità · 20'</div>
    <div style="flex:20;background:var(--verde)">Attacco-difesa · 20'</div>
    <div style="flex:20;background:#7aa995">Punizioni · 20'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il tema è il <b>cambio di ritmo</b>: in partita si gioca con più tocchi nella propria metà e con meno tocchi in quella avversaria, quindi la palla deve accelerare man mano che si avvicina alla porta. Poi il lavoro di rapidità allena le gambe a fare lo stesso.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita cambio di ritmo (4-2-3-1 contro 4-2-3-1)
def campo_partita():
    # la squadra blu attacca a destra (il suo lato destro è in basso)
    blu = (g(90, 60, "pB") + g(90, 120, "pB") + g(90, 180, "pB") + g(90, 240, "pB")
           + g(160, 110, "pB") + g(160, 190, "pB")
           + g(225, 60, "pB") + g(225, 145, "pB") + g(225, 240, "pB")
           + g(310, 130, "pB"))
    rossi = (g(410, 60, "pA") + g(410, 120, "pA") + g(410, 180, "pA") + g(410, 240, "pA")
             + g(340, 105, "pA") + g(340, 195, "pA")
             + g(275, 70, "pA") + g(275, 160, "pA") + g(275, 235, "pA")
             + g(190, 232, "pA"))
    return f'''<svg class="diagram" viewBox="0 0 500 310" style="width:118mm;margin:0 auto">
    <rect x="0" y="0" width="500" height="310" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/>
      <rect x="16" y="125" width="14" height="50"/><rect x="470" y="125" width="14" height="50"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">3/4 DELLA LUNGHEZZA DEL CAMPO</text>
    <g font-family="Oswald" font-size="11" fill="#fff" text-anchor="middle" letter-spacing="1">
      <text x="140" y="298">METÀ DIFENSIVA BLU · 3 TOCCHI</text>
      <text x="360" y="298">METÀ OFFENSIVA BLU · 2 TOCCHI</text>
    </g>
    {g(42, 150, "pP")}{g(458, 150, "pP")}
    {rossi}{blu}
    {freccia("M102,180 L148,190", tratteggio=True)}{freccia("M172,188 L214,150", tratteggio=True)}{freccia("M237,143 L298,132", tratteggio=True)}
    <use href="#palla" x="98" y="192"/>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita “cambio di ritmo”</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti · 2 tempi da 15'</span><span class="chip">10 contro 10 + portieri</span><span class="chip">Campo lungo 3/4</span><span class="chip">Diviso in 2 metà</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> cambiare ritmo man mano che ci si avvicina alla porta. Nella propria metà si costruisce con più tocchi, in quella avversaria la palla deve viaggiare più veloce.</p>
  {campo_partita()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Metà difensiva: massimo <b>3 tocchi</b></li>
        <li>Metà offensiva: massimo <b>2 tocchi</b></li>
        <li>Vietato passare al compagno di reparto</li>
        <li>Gol valido solo se <b>tutti sono nella metà offensiva</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Metà difensiva: massimo <b>2 tocchi</b></li>
        <li>Metà offensiva: <b>1 tocco</b></li>
        <li>Gol valido solo se <b>tutti sono nella metà offensiva</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo lungo 3/4 del regolamentare e largo quanto il campo, diviso in due metà</li>
      <li>Due squadre da 10 con il 4-2-3-1</li>
      <li>Due porte con i portieri</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Partita con porte. Il numero di tocchi cambia a seconda della metà campo in cui si trova la palla.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Superata la metà, accelerare la giocata</li>
      <li>Smarcarsi prima per giocare di prima</li>
      <li>Salire tutti insieme per rendere valido il gol</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Rapidità
stazioni = [
    ("Slalom + scatto", "slalom tra 4 conetti o paletti, poi 10 m di scatto", "7 volte"),
    ("Skip + scatto", "5 m di skip alto, basso o calciato, poi 10 m di scatto", "9 volte"),
    ("Scaletta + scatto", "scaletta, poi 10 m di scatto", ""),
    ("Partenze da seduti", "10 m di scatto partendo seduti: verso destra, sinistra, avanti, dietro", "8 volte"),
]
st_html = "".join(
    f'<div class="stazione"><div class="n">{i}</div><div><div class="t">{t}</div>'
    + (f'<div class="d">{d}</div>' if d else "") + f'</div><div class="q">{q}</div></div>'
    for i, (t, d, q) in enumerate(stazioni, 1))

rapidita = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Rapidità</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti</span><span class="chip">4 stazioni</span><span class="chip">Scatti da 10 m</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> rapidità e reattività. Ogni stazione finisce con uno scatto di 10 metri.</p>
  <div class="stazioni">{st_html}</div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>4 stazioni in sequenza</li>
      <li>Conetti o paletti, una scaletta, 10 m segnati dopo ogni stazione</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Nella stazione 2 le 9 ripetizioni sono <b>3 per ogni tipo di skip</b>.</p>
      <p>Nella stazione 4 si parte seduti guardando ogni volta in una direzione diversa.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Massima velocità in ogni scatto</li>
      <li>Appoggi rapidi nello slalom e nella scaletta</li>
      <li>Recuperare completamente prima della ripetizione successiva</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 5. Attacco contro difesa + punizioni difensive
attacco_svg = mezzo_campo(
    # chi difende: 4-2-3-1 senza il trequartista
    g(110, 140, "pB", 2) + g(200, 135, "pB", 5) + g(300, 135, "pB", 6) + g(390, 140, "pB", 3)
    + g(205, 200, "pB", 4) + g(295, 200, "pB", 8)
    + g(75, 240, "pB", 7) + g(425, 240, "pB", 11) + g(250, 300, "pB", 9)
    + g(40, 180, "pA") + g(150, 180, "pA") + g(250, 175, "pA") + g(350, 180, "pA") + g(460, 180, "pA")
    + g(140, 255, "pA") + g(250, 250, "pA") + g(360, 255, "pA") + g(250, 348, "pA")
    + '<use href="#palla" x="262" y="356"/>', "112mm")

attacco = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Attacco contro difesa</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti · 2 tempi da 10'</span><span class="chip">9 contro 9 + portiere</span><span class="chip">Conduce l'allenatore</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> come nell'Allenamento 6, curare i movimenti difensivi in situazione di gioco e poi quelli offensivi, senza fermare il gioco.</p>
  {attacco_svg}

  <div class="kicker" style="margin-top:7mm">Esercitazione V</div>
  <div class="ex-title"><h2 style="font-size:17pt">Punizioni difensive e stretching · 20'</h2></div>
  <div class="two" style="margin-top:3mm">
    <div class="box"><h4>Punizioni difensive</h4>Lavoro sulle punizioni a sfavore.</div>
    <div class="box"><h4>Stretching finale</h4>Allungamento dei principali gruppi muscolari a fine seduta.</div>
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, partita, rapidita, attacco]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-07.html").write_text(html)
print("pagine:", PAG[0])
