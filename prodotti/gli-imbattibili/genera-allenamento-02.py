"""Genera allenamento-02.html partendo dallo stile dell'Allenamento 1."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()

# Testa, stili e simboli SVG condivisi
testa = a1[: a1.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 1</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 2</title>")
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("allenamento-01.jpg", "allenamento-02.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 2")
             .replace("la prima seduta della Juniores", "la seconda seduta della Juniores"))
ricerca = re.search(r'<!-- 3. PARTITA RICERCA DEL PORTIERE -->\s*(<section class="page">.*?</section>)', a1, re.S).group(1)

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 2</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def mezzo_campo(contenuto):
    return f'''<svg class="diagram" viewBox="0 0 500 380" style="width:150mm;margin:0 auto">
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
      <div class="kicker">Precampionato · Settimana 1</div>
      <h2>Allenamento 2</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">105'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">50 m × largh.</div></div>
    <div><div class="l">Focus</div><div class="v">Difesa sul lancio</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">Attivazione generale</div></td><td class="min">10'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “ricerca del portiere”</div><div class="d">Seconda versione: tocchi e punteggi diversi, nel 2° tempo solo gioco verticale</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Lavoro a gruppi con cambio</div><div class="d">Gruppo A: linea difensiva con l'allenatore (3 progressioni) · Gruppo B: gioco di posizione 4 contro 4 + 2 jolly</div></td><td class="min">30'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Lavoro aerobico</div><div class="d">Corsa con variazioni di velocità · 2 blocchi da 10'</div></td><td class="min">25'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Defaticamento</div><div class="d">Stretching ed esercizi di scarico della colonna vertebrale</div></td><td class="min">10'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:10;background:#7aa995">10'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:30;background:var(--verde)">Lavoro a gruppi · 30'</div>
    <div style="flex:25;background:var(--oro);color:var(--verde)">Aerobico · 25'</div>
    <div style="flex:10;background:#7aa995">10'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    Il tema del giorno è il <b>lancio</b>: in partita chi attacca è premiato quando cerca la profondità, mentre nel lavoro a gruppi la linea difensiva impara a leggerlo e a respingerlo.
  </div>
  {footer()}
</section>'''

# ---------- 3. Ricerca del portiere (versione 2)
r = ricerca
r = r.replace("<span>Precampionato · Allenamento 1</span><span>3</span>", "<span>Precampionato · Allenamento 2</span><span>3</span>")
PAG[0] += 1
r = re.sub(r'<h4>1° tempo · 15\'</h4>.*?</ul>', '''<h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li>Portiere trovato dalla metà offensiva: <b>1 punto</b></li>
        <li>Portiere trovato con un lancio dalla metà difensiva: <b>2 punti</b></li>
      </ul>''', r, count=1, flags=re.S)
r = re.sub(r'<h4>2° tempo · 15\'</h4>.*?</ul>', '''<h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li>Stesso punteggio del 1° tempo</li>
        <li><b>Solo gioco verticale</b></li>
      </ul>''', r, count=1, flags=re.S)
r = r.replace("Nel secondo tempo cambiano tocchi e punteggio (vedi riquadri sopra).",
              "Rispetto all'Allenamento 1 il lancio dalla metà difensiva vale 2 punti fin dal primo tempo.")
r = r.replace("<li>Nel 2° tempo cercare la profondità appena c'è spazio</li>",
              "<li>Cercare la profondità appena c'è spazio</li>")
r = r.replace('<p class="obj"><b>Obiettivo:</b> possesso palla orientato alla profondità. Smarcarsi, giocare a pochi tocchi e servire il compagno più avanzato appena possibile.</p>',
              '<p class="obj"><b>Obiettivo:</b> possesso palla orientato alla profondità. Rispetto all\'Allenamento 1 la squadra è spinta ancora di più a giocare in verticale e a cercare il lancio.</p>')
ricerca2 = r

# ---------- 4-6. Linea difensiva
ld1 = pagina_esercizio(
    "Esercitazione III · Gruppo A · Progressione 1 di 3", "Attenti al lancio in esterna",
    "leggere in anticipo il lancio verso la fascia e respingere la palla.",
    mezzo_campo(
        freccia("M140,152 L172,152", True) + freccia("M220,152 L252,152", True) + freccia("M300,152 L332,152", True)
        + freccia("M388,150 L420,178", True)
        + freccia("M160,322 Q300,250 430,196", tratteggio=True)
        + g(50, 230, "pA") + g(150, 330, "pA") + g(260, 338, "pA") + g(370, 330, "pA") + g(445, 200, "pA")
        + '<use href="#palla" x="165" y="338"/>'
        + g(130, 152, "pB", 2) + g(210, 152, "pB", 6) + g(290, 152, "pB", 5) + g(380, 146, "pB", 3)
        + '<text x="300" y="268" font-family="Oswald" font-size="12" fill="#fff" letter-spacing="2" transform="rotate(-22 300 268)">LANCIO</text>'),
    "<li>Linea a 4 + portiere</li><li>Attaccanti che muovono la palla davanti alla linea</li><li>Metà campo con area di rigore</li>",
    "<p>Gli attaccanti muovono la palla da destra a sinistra e viceversa. La linea difensiva <b>scivola</b> posizionandosi in funzione della palla.</p>"
    "<p>A turno un attaccante fa un <b>lancio in esterna</b>: la linea deve leggerlo e <b>respingere la palla</b>.</p>",
    "<li>Scivolare insieme seguendo la palla</li><li>Leggere il lancio prima che parta</li><li>Il difensore più vicino attacca la palla</li><li>Gli altri coprono il compagno</li>",
    chips='<span class="chip">30 minuti con il cambio</span><span class="chip">Conduce l\'allenatore</span>')

ld2 = pagina_esercizio(
    "Esercitazione III · Gruppo A · Progressione 2 di 3", "Ti lascio alle spalle",
    "difendere sulla giocata verso l'attaccante, scegliendo se anticipare o non farlo girare.",
    mezzo_campo(
        freccia("M95,322 L95,262", tratteggio=True)
        + freccia("M118,205 L104,228", True) + freccia("M160,128 L138,152", True) + freccia("M240,128 L222,140", True)
        + g(95, 335, "pA") + g(95, 250, "pA") + g(230, 325, "pA") + g(420, 300, "pA") + g(430, 200, "pA")
        + '<use href="#palla" x="110" y="342"/>'
        + g(120, 195, "pB", 5) + g(160, 120, "pB", 2) + g(250, 120, "pB", 6) + g(345, 120, "pB", 3)),
    "<li>Linea a 4 + portiere</li><li>Un difensore (il 5) segue l'attaccante che viene incontro</li><li>Metà campo con area di rigore</li>",
    "<p>Gli attaccanti muovono la palla come in figura. Quando arriva la <b>giocata sull'attaccante</b> la linea deve respingere la palla oppure <b>non far giocare l'attaccante</b>, a seconda di come arriva la palla.</p>"
    "<p>Nel frattempo gli altri difensori si muovono per coprire lo spazio lasciato libero.</p>",
    "<li>Palla che arriva lenta: anticipare</li><li>Palla tesa: stare attaccati e non far girare l'attaccante</li><li>Chi resta dietro copre lo spazio alle spalle</li>")

ld3 = pagina_esercizio(
    "Esercitazione III · Gruppo A · Progressione 3 di 3", "6 contro 4",
    "respingere il lancio e difendere subito in inferiorità numerica.",
    mezzo_campo(
        freccia("M245,322 Q230,240 262,178", tratteggio=True)
        + freccia("M292,150 L272,168", True)
        + g(40, 205, "pA") + g(460, 205, "pA") + g(100, 320, "pA") + g(245, 335, "pA") + g(400, 320, "pA") + g(245, 158, "pA")
        + '<use href="#palla" x="260" y="342"/>'
        + g(120, 150, "pB", 2) + g(195, 150, "pB", 5) + g(300, 150, "pB", 6) + g(375, 150, "pB", 3)),
    "<li>Linea a 4 + portiere</li><li>6 attaccanti: uno in mezzo alla linea, due larghi, tre dietro</li><li>Metà campo con area di rigore</li>",
    "<p>Gli attaccanti muovono la palla da destra a sinistra. A un certo punto un attaccante fa un <b>lancio verso la linea</b>.</p>"
    "<p>La linea <b>respinge</b> e da quel momento l'azione continua come una partita <b>6 contro 4</b>.</p>",
    "<li>Respingere lontano dalla porta</li><li>Dopo la respinta la linea esce insieme</li><li>In inferiorità: restare compatti e proteggere la porta</li>")

# ---------- 7. Gioco di posizione
def gp():
    pl = (g(250, 30, "pJ", 9, "#1d2421") + g(250, 105, "pJ", 10, "#1d2421")
          + g(110, 140, "pB", 11) + g(390, 150, "pB", 7) + g(185, 180, "pB", 4) + g(275, 310, "pB", 5)
          + g(110, 250, "pA", 3) + g(390, 240, "pA", 2) + g(225, 268, "pA", 6) + g(305, 170, "pA", 8))
    return f'''<svg class="diagram" viewBox="0 0 500 340" style="width:150mm;margin:0 auto">
    <rect width="500" height="340" fill="url(#strisce)"/>
    <rect x="110" y="30" width="280" height="280" fill="none" stroke="#fff" stroke-width="2.5"/>
    <text x="250" y="332" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    <text x="430" y="175" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    {freccia("M196,172 L240,116", tratteggio=True)}{freccia("M261,110 L376,147", tratteggio=True)}
    <use href="#palla" x="200" y="192"/>
    {pl}
  </svg>'''

gioco = f'''<section class="page">
  <div class="kicker">Esercitazione III · Gruppo B</div>
  <div class="ex-title"><h2>Gioco di posizione</h2></div>
  <div class="ex-sub">
    <span class="chip">4 contro 4 + 2 jolly</span><span class="chip">Campo 30 × 30 m</span><span class="chip">3 serie da 4'</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> consolidare lo smarcamento. Ogni giocatore deve muoversi per offrire sempre una soluzione di passaggio.</p>
  {gp()}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Quadrato di 30 × 30 metri</li>
      <li>Due squadre da 4 giocatori</li>
      <li>2 jolly: il 9 e il 10</li>
      <li>3 serie da 4 minuti</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>La squadra in possesso, aiutata dai due jolly, cerca di tenere palla. Ogni <b>15 passaggi consecutivi</b> vale <b>1 gol</b>.</p>
      <p>Al termine delle serie <b>si invertono i gruppi</b> con la linea difensiva.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Smarcarsi prima che il compagno riceva</li>
      <li>Muoversi negli spazi liberi, lontano dall'avversario</li>
      <li>Usare i jolly per uscire dalla pressione</li>
      <li>Pochi tocchi e palla che viaggia veloce</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 8. Lavoro aerobico + defaticamento
def blocco(x0, w):
    """Barre lento/veloce: 1' lento + 30'' veloce ripetuti."""
    out, x, unit = [], x0, w / 10  # 10 minuti
    while x < x0 + w - 0.1:
        l = min(unit, x0 + w - x)
        out.append(f'<rect x="{x:.1f}" y="70" width="{l:.1f}" height="40" fill="#7aa995"/>')
        x += l
        if x >= x0 + w - 0.1:
            break
        v = min(unit / 2, x0 + w - x)
        out.append(f'<rect x="{x:.1f}" y="45" width="{v:.1f}" height="65" fill="#d4a017"/>')
        x += v
    return "".join(out)

aerobico_svg = f'''<svg class="diagram" viewBox="0 0 500 170" style="margin:2mm 0 5mm">
    <rect width="500" height="170" rx="6" fill="#f3f5f2"/>
    {blocco(20, 190)}
    <rect x="215" y="85" width="70" height="25" fill="#c9d6cf"/>
    {blocco(290, 190)}
    <line x1="20" y1="110" x2="480" y2="110" stroke="#1d2421" stroke-width="1.5"/>
    <g font-family="Oswald" font-size="13" text-anchor="middle" fill="#0f3d2e">
      <text x="115" y="32">BLOCCO 1 · 10'</text><text x="250" y="77">RECUPERO</text><text x="250" y="132" font-size="11">attivo 5'</text><text x="385" y="32">BLOCCO 2 · 10'</text>
    </g>
    <g font-family="Inter" font-size="11" fill="#5d6b65">
      <rect x="20" y="145" width="14" height="10" fill="#7aa995"/><text x="40" y="154">1' corsa lenta</text>
      <rect x="140" y="145" width="14" height="10" fill="#d4a017"/><text x="160" y="154">30" corsa veloce</text>
    </g>
  </svg>'''

aerobico = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Lavoro aerobico</h2></div>
  <div class="ex-sub">
    <span class="chip">25 minuti</span><span class="chip">Corsa con variazioni di velocità (CCVV)</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> incremento della capacità e della potenza aerobica.</p>
  {aerobico_svg}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>2 blocchi da 10 minuti</li>
      <li>5 minuti di recupero attivo tra i blocchi</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>In ogni blocco si alterna <b>1 minuto di corsa lenta</b> e <b>30 secondi di corsa veloce</b>, senza fermarsi.</p>
      <p>Nel recupero attivo si continua a muoversi con corsa leggera o camminata.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Il tratto veloce è sostenuto, non uno sprint massimale</li>
      <li>Il tratto lento serve a recuperare: non fermarsi</li>
      <li>Mantenere lo stesso ritmo dal primo all'ultimo veloce</li>
    </ul></div>
  </div>

  <div class="kicker" style="margin-top:7mm">Esercitazione V</div>
  <div class="ex-title"><h2 style="font-size:17pt">Defaticamento · 10'</h2></div>
  <div class="two" style="margin-top:3mm">
    <div class="box"><h4>Stretching</h4>Allungamento dei principali gruppi muscolari a fine seduta.</div>
    <div class="box"><h4>Scarico della colonna</h4>Esercizi di scarico della colonna vertebrale dopo il lavoro di corsa.</div>
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n" + scheda + "\n\n" + ricerca2 + "\n\n"
        + "\n\n".join([ld1, ld2, ld3, gioco, aerobico]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-02.html").write_text(html)
print("pagine:", PAG[0])
