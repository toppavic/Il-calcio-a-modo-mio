"""Genera allenamento-12.html partendo dallo stile dell'Allenamento 2.

Dall'Allenamento 12 comincia il campionato: sedute il lunedì e il giovedì.
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

N = 12
TESTO_PIEDE = f"In campionato · Allenamento {N}"

# Testa, stili e simboli SVG condivisi
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      f"<title>Gli Imbattibili – In campionato, Allenamento {N}</title>")
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("precampionato/allenamento-01.jpg", f"campionato/allenamento-{N}.jpg")
             .replace("Precampionato · Allenamento 1", TESTO_PIEDE)
             .replace("la prima seduta della Juniores",
                      "la prima seduta di campionato della Juniores"))

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
      <div class="kicker">In campionato · Seduta del lunedì</div>
      <h2>Allenamento {N}</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">circa 100'</div></div>
    <div><div class="l">Giocatori</div><div class="v">7 contro 7</div></div>
    <div><div class="l">Campo</div><div class="v">35 m + 2 mete da 5 m</div></div>
    <div><div class="l">Focus</div><div class="v">Arrivare in meta e attacco contro difesa</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita a meta</div><div class="d">7 contro 7 · 3 tempi da 10' · entrati in meta si segna in una delle 3 porticine · tocchi che scendono da 3 a 2</div></td><td class="min">35'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Attacco contro difesa</div><div class="d">7 contro 7 · 2 tempi da 15' · tocco libero</div></td><td class="min">35'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Corsa con variazioni di velocità</div><div class="d">Sulla metà campo: lato corto di recupero, diagonale in allungo</div></td><td class="min">9'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Stretching</div><div class="d">Defaticamento finale</div></td><td class="min">10'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:35;background:var(--verde-2)">Partita a meta · 35'</div>
    <div style="flex:35;background:var(--verde)">Attacco-difesa · 35'</div>
    <div style="flex:9;background:var(--oro);color:var(--verde)">9'</div>
    <div style="flex:10;background:#7aa995">10'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Comincia il campionato e cambia il ritmo della settimana: si lavora il <b>lunedì</b> e il <b>giovedì</b>.
    Il lunedì si riparte dal pallone: una partita dove bisogna <b>portare la palla in meta</b> e poi
    l'<b>attacco contro difesa</b>, con un lavoro di corsa corto prima dello stretching.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita a meta
meta = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita a meta</h2></div>
  <div class="ex-sub">
    <span class="chip">35 minuti · 3 tempi da 10'</span><span class="chip">7 contro 7</span><span class="chip">35 m + 2 mete da 5 m</span><span class="chip">3 porticine per lato</span>
  </div>
  <p class="obj" style="margin-top:1mm"><b>Obiettivo:</b> attaccare lo spazio e arrivare in meta palla al piede, poi rifinire subito l'azione scegliendo la porticina libera. Tempo dopo tempo i tocchi calano e il gioco si fa più veloce.</p>
  <div style="display:flex;gap:6mm;align-items:center">
    <div style="flex:1">{campo_meta("100%")}</div>
    <div style="flex:1;display:flex;flex-direction:column;gap:3mm">
      <div class="box"><h4>1° tempo · 10'</h4><ul class="clean"><li>Massimo <b>3 tocchi</b></li></ul></div>
      <div class="box"><h4>2° tempo · 10'</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li></ul></div>
      <div class="box"><h4>3° tempo · 10'</h4><ul class="clean"><li>Massimo <b>2 tocchi</b></li><li>Gol su <b>ripartenza</b>: 1 gol</li></ul></div>
    </div>
  </div>
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo di gioco lungo 35 m con una meta di 5 m per lato</li>
      <li>3 porticine (1, 2, 3) dietro ogni meta</li>
      <li>Due squadre da 7</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Ogni squadra attacca una meta. <b>Una volta entrati in meta</b> si fa gol in una delle tre porticine.</p>
      <p>Nei tre tempi cambiano i tocchi (vedi riquadri sopra).</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Attaccare la meta appena c'è spazio</li>
      <li>Entrati in meta, testa alta per scegliere la porticina libera</li>
      <li>Chi difende protegge la meta prima delle porticine</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 4. Attacco contro difesa + CCVV + stretching
def x_(x):
    return round(60 + (x - 35) * 1.767)


attacco_svg = f'''<svg class="diagram" viewBox="0 0 500 380" style="width:104mm;margin:0 auto">
    <rect width="500" height="380" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="40" y="22" width="420" height="336"/>
      <rect x="205" y="10" width="90" height="12"/><rect x="205" y="358" width="90" height="12"/>
    </g>
    {g(250, 38, "pP")}{g(250, 342, "pP")}
    {g(x_(85), 90, "pB")}{g(x_(160), 96, "pB")}{g(x_(213), 90, "pB")}
    {g(x_(55), 200, "pB")}{g(x_(153), 196, "pB")}{g(x_(232), 200, "pB")}{g(x_(152), 250, "pB")}
    {g(x_(145), 106, "pA")}{g(x_(128), 212, "pA")}{g(x_(180), 212, "pA")}
    {g(x_(65), 290, "pA")}{g(x_(125), 280, "pA")}{g(x_(182), 280, "pA")}{g(x_(228), 290, "pA")}
    <use href="#palla" x="{x_(125) + 14}" y="292"/>
    {freccia(f"M{x_(125)},266 L{x_(128)+4},224", tratteggio=True)}
  </svg>'''

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

attacco = f'''<section class="page">
  <div class="kicker">Esercitazione III</div>
  <div class="ex-title"><h2>Attacco contro difesa</h2></div>
  <div class="ex-sub">
    <span class="chip">35 minuti · 2 tempi da 15'</span><span class="chip">7 contro 7</span><span class="chip">Tocco libero</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> sette contro sette su un campo con due porte, a tocco libero: chi attacca (rossi) cerca il gol, chi difende (blu) lavora di reparto e, se recupera, riparte verso l'altra porta.</p>
  {attacco_svg}

  <div class="kicker" style="margin-top:6mm">Esercitazione IV</div>
  <div class="ex-title"><h2 style="font-size:17pt">Corsa con variazioni di velocità · 9'</h2></div>
  <div style="display:flex;gap:6mm;align-items:center;margin-top:3mm">
    <div style="flex:1.1">{ccvv_svg}</div>
    <div class="box" style="flex:1">Si corre sulla <b>metà campo</b> per 9 minuti senza fermarsi:
      <b>lato corto</b> di corsa lenta per recuperare, <b>diagonale</b> in allungo.</div>
  </div>

  <div class="chiave">
    <span class="kicker">Esercitazione V · stretching · 10'</span>
    Allungamento dei principali gruppi muscolari a fine seduta.
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, meta, attacco]) + "\n\n</body>\n</html>\n")
(QUI / f"allenamento-{N}.html").write_text(html)
print("pagine:", PAG[0])
