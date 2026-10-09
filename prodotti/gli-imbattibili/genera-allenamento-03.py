"""Genera allenamento-03.html: stile dell'Allenamento 1, linea difensiva ripresa dall'Allenamento 2."""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
a1 = (QUI / "allenamento-01.html").read_text()
a2 = (QUI / "allenamento-02.html").read_text()

# Testa, stili e simboli SVG condivisi (quelli dell'Allenamento 2 includono già le fasi)
testa = a2[: a2.index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 2</title>",
                      "<title>Gli Imbattibili – Precampionato, Allenamento 3</title>")
copertina = re.search(r'<section class="page c5">.*?</section>', a1, re.S).group(0)
copertina = (copertina
             .replace("allenamento-01.jpg", "allenamento-03.jpg")
             .replace("Precampionato · Allenamento 1", "Precampionato · Allenamento 3")
             .replace("la prima seduta della Juniores", "la terza seduta della Juniores"))
pagine_a2 = re.findall(r'<section class="page">.*?</section>', a2, re.S)

PAG = [1]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>GLI IMBATTIBILI</b><span>Precampionato · Allenamento 3</span>'
            f'<span>{PAG[0]}</span></div>')


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def da_allenamento_2(pagina, minuti=False):
    """Riprende una pagina dell'Allenamento 2 con piè di pagina e tempi aggiornati."""
    p = re.sub(r'<div class="footer">.*?</div>', footer(), pagina, count=1, flags=re.S)
    if minuti:
        p = p.replace("15 minuti per gruppo, poi cambio", "20 minuti per gruppo, poi cambio")
    return p


# ---------- 2. Scheda seduta
scheda = f'''<section class="page">
  <div class="head">
    <div>
      <div class="kicker">Precampionato · Settimana 1</div>
      <h2>Allenamento 3</h2>
    </div>
  </div>

  <div class="meta">
    <div><div class="l">Durata</div><div class="v">125'</div></div>
    <div><div class="l">Giocatori</div><div class="v">22</div></div>
    <div><div class="l">Campo</div><div class="v">50 m × largh.</div></div>
    <div><div class="l">Focus</div><div class="v">Gioco tra i reparti</div></div>
  </div>

  <h3>Programma della seduta</h3>
  <table class="programma">
    <tr><td class="num">I</td><td><div class="t">Riscaldamento</div><div class="d">10' di attivazione + 5' di combinazioni di passaggio in cerchio</div></td><td class="min">15'</td></tr>
    <tr><td class="num">II</td><td><div class="t">Partita “no compagno di reparto”</div><div class="d">10 contro 10 · vietato passare la palla al compagno del proprio reparto · chi perde paga con i suicidi a fine allenamento</div></td><td class="min">30'</td></tr>
    <tr><td class="num">III</td><td><div class="t">Lavoro a gruppi con cambio</div><div class="d">20' per gruppo · Gruppo A: linea difensiva con l'allenatore (le 3 progressioni dell'Allenamento 2) · Gruppo B: gioco di posizione 4 contro 4 + 2 jolly a tocchi limitati. Poi si invertono</div></td><td class="min">40'</td></tr>
    <tr><td class="num">IV</td><td><div class="t">Lavoro atletico</div><div class="d">Corsa con variazioni di velocità · 2 blocchi da 12'</div></td><td class="min">30'</td></tr>
    <tr><td class="num">V</td><td><div class="t">Defaticamento</div><div class="d">Stretching</div></td><td class="min">10'</td></tr>
  </table>

  <div class="timeline">
    <div style="flex:15;background:#7aa995">15'</div>
    <div style="flex:30;background:var(--verde-2)">Partita · 30'</div>
    <div style="flex:40;background:var(--verde)">Lavoro a gruppi · 20' + 20'</div>
    <div style="flex:30;background:var(--oro);color:var(--verde)">Atletico · 30'</div>
    <div style="flex:10;background:#7aa995">10'</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il filo della seduta</span>
    La palla deve <b>passare da un reparto all'altro</b>: in partita è vietato appoggiarsi al compagno vicino, nel gioco di posizione i tocchi si riducono. Intanto la linea difensiva ripete il lavoro del giorno prima per renderlo automatico.
  </div>
  {footer()}
</section>'''

# ---------- 3. Partita no compagno di reparto
def campo_partita():
    blu = (g(85, 55, "pB") + g(85, 115, "pB") + g(85, 185, "pB") + g(85, 245, "pB")
           + g(185, 55, "pB") + g(185, 120, "pB") + g(185, 185, "pB") + g(185, 250, "pB")
           + g(300, 110, "pB") + g(300, 195, "pB"))
    rossi = (g(422, 70, "pA") + g(422, 135, "pA") + g(422, 200, "pA") + g(390, 250, "pA")
             + g(320, 55, "pA") + g(330, 150, "pA") + g(320, 240, "pA") + g(270, 255, "pA")
             + g(215, 90, "pA") + g(215, 210, "pA"))
    vietato = (f'{freccia("M85,172 L85,130", tratteggio=True)}'
               '<g stroke="#e8433a" stroke-width="4" stroke-linecap="round"><path d="M75,141 L95,161"/><path d="M95,141 L75,161"/></g>'
               '<text x="102" y="150" font-family="Oswald" font-size="13" font-weight="700" fill="#fff">NO</text>')
    ok = (freccia("M97,180 L172,126", tratteggio=True)
          + '<text x="142" y="172" font-family="Oswald" font-size="13" font-weight="700" fill="#fff">SÌ</text>')
    return f'''<svg class="diagram" viewBox="0 0 500 300" style="width:118mm;margin:0 auto">
    <rect x="0" y="0" width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/>
      <line x1="250" y1="20" x2="250" y2="280"/>
      <rect x="16" y="125" width="14" height="50"/><rect x="470" y="125" width="14" height="50"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" opacity=".9">50 m</text>
    {g(42, 150, "pP")}{g(458, 150, "pP")}
    {rossi}{blu}
    {vietato}{ok}
    <use href="#palla" x="99" y="194"/>
  </svg>'''

partita = f'''<section class="page">
  <div class="kicker">Esercitazione II</div>
  <div class="ex-title"><h2>Partita “no compagno di reparto”</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti</span><span class="chip">10 contro 10 + portieri</span><span class="chip">Campo 50 m × tutta la larghezza</span><span class="chip">Diviso in 2 metà</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> far viaggiare la palla tra i reparti. Senza l'appoggio al compagno vicino ogni giocatore deve cercare una linea di passaggio più avanti o più indietro.</p>
  {campo_partita()}

  <div class="two">
    <div class="box">
      <h4>1° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>3 tocchi</b></li>
        <li><b>Vietato</b> passare al compagno del proprio reparto</li>
        <li>Ogni gol vale <b>1 punto</b></li>
      </ul>
    </div>
    <div class="box">
      <h4>2° tempo · 15'</h4>
      <ul class="clean">
        <li>Massimo <b>2 tocchi</b></li>
        <li><b>Vietato</b> passare al compagno del proprio reparto</li>
        <li>Gol dopo un <b>recupero palla nella metà offensiva</b>: <b>2 punti</b></li>
      </ul>
    </div>
  </div>

  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Campo lungo 50 m e largo quanto il campo regolamentare, diviso in due metà</li>
      <li>Due squadre da 10 giocatori più i portieri</li>
      <li>Una porta per ogni lato corto</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Partita normale con una regola: la palla non può andare a un compagno dello <b>stesso reparto</b> (difensore a difensore, centrocampista a centrocampista, attaccante ad attaccante).</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Smarcarsi tra le linee per dare il passaggio al reparto vicino</li>
      <li>Testa alta prima di ricevere</li>
      <li>Nel 2° tempo pressare alto: il recupero avanti vale doppio</li>
    </ul></div>
  </div>

  <div class="chiave">
    <span class="kicker">La posta in gioco · suicidi a fine allenamento</span>
    Chi perde: <b>5 suicidi</b> · chi vince: <b>2 suicidi</b> · pareggio: <b>3 suicidi per tutti</b>. Il suicidio è una navetta dal limite dell'area piccola al limite dell'area grande.
  </div>
  {footer()}
</section>'''

# ---------- 4-6. Linea difensiva: le tre progressioni dell'Allenamento 2
ld1 = da_allenamento_2(pagine_a2[2], minuti=True).replace(
    '<span class="chip">Conduce l\'allenatore</span>',
    '<span class="chip">Conduce l\'allenatore</span><span class="chip">Come nell\'Allenamento 2</span>')
ld2 = da_allenamento_2(pagine_a2[3])
ld3 = da_allenamento_2(pagine_a2[4])

# ---------- 7. Gioco di posizione (più difficile)
def gp():
    pl = (g(250, 30, "pJ", 9, "#1d2421") + g(250, 105, "pJ", 10, "#1d2421")
          + g(140, 120, "pB", 11) + g(185, 200, "pB", 4) + g(370, 225, "pB", 2) + g(235, 280, "pB", 5)
          + g(360, 110, "pA", 7) + g(235, 190, "pA", 8) + g(140, 275, "pA", 3) + g(305, 270, "pA", 6))
    return f'''<svg class="diagram" viewBox="0 0 500 340" style="width:150mm;margin:0 auto">
    <rect width="500" height="340" fill="url(#strisce)"/>
    <rect x="110" y="30" width="280" height="280" fill="none" stroke="#fff" stroke-width="2.5"/>
    <text x="250" y="332" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    <text x="430" y="175" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    {freccia("M180,188 L240,117", tratteggio=True)}{freccia("M261,110 L361,214", tratteggio=True)}
    <use href="#palla" x="190" y="214"/>
    {pl}
  </svg>'''

gioco = f'''<section class="page">
  <div class="kicker">Esercitazione III · Gruppo B</div>
  <div class="ex-title"><h2>Gioco di posizione a tocchi limitati</h2></div>
  <div class="ex-sub">
    <span class="chip">20 minuti, poi cambio</span><span class="chip">4 contro 4 + 2 jolly</span><span class="chip">Campo 30 × 30 m</span><span class="chip">2 tocchi · jolly 1 tocco</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> smarcamento. È il gioco di posizione dell'Allenamento 2 reso più difficile: con meno tocchi bisogna smarcarsi prima e più velocemente.</p>
  {gp()}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>Quadrato di 30 × 30 metri</li>
      <li>Due squadre da 4 giocatori</li>
      <li>2 jolly: il 9 e il 10</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>Stesse regole dell'Allenamento 2: ogni <b>8 passaggi consecutivi</b> vale <b>1 punto</b>.</p>
      <p>Si gioca a <b>2 tocchi</b>, mentre i jolly hanno <b>1 solo tocco</b>.</p>
    </div>
    <div class="box"><h4>Punti chiave</h4><ul class="clean">
      <li>Sapere già a chi passare prima di ricevere</li>
      <li>Il jolly va servito quando ha già una soluzione pronta</li>
      <li>Smarcarsi subito dopo aver passato</li>
    </ul></div>
  </div>
  {footer()}
</section>'''

# ---------- 8. Lavoro atletico + defaticamento
def blocco(x0, w, minuti):
    """Barre lento/veloce: 1' lento + 30'' veloce ripetuti."""
    out, x, unit = [], x0, w / minuti
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

atletico_svg = f'''<svg class="diagram" viewBox="0 0 500 170" style="margin:2mm 0 5mm">
    <rect width="500" height="170" rx="6" fill="#f3f5f2"/>
    {blocco(20, 195, 12)}
    <rect x="220" y="85" width="60" height="25" fill="#c9d6cf"/>
    {blocco(285, 195, 12)}
    <line x1="20" y1="110" x2="480" y2="110" stroke="#1d2421" stroke-width="1.5"/>
    <g font-family="Oswald" font-size="13" text-anchor="middle" fill="#0f3d2e">
      <text x="117" y="32">BLOCCO 1 · 12'</text><text x="250" y="77">RECUPERO</text><text x="250" y="132" font-size="11">5'</text><text x="382" y="32">BLOCCO 2 · 12'</text>
    </g>
    <g font-family="Inter" font-size="11" fill="#5d6b65">
      <rect x="20" y="145" width="14" height="10" fill="#7aa995"/><text x="40" y="154">1' corsa lenta</text>
      <rect x="140" y="145" width="14" height="10" fill="#d4a017"/><text x="160" y="154">30" corsa veloce</text>
    </g>
  </svg>'''

atletico = f'''<section class="page">
  <div class="kicker">Esercitazione IV</div>
  <div class="ex-title"><h2>Lavoro atletico</h2></div>
  <div class="ex-sub">
    <span class="chip">30 minuti</span><span class="chip">Corsa con variazioni di velocità (CCVV)</span>
  </div>
  <p class="obj"><b>Obiettivo:</b> incremento della capacità e della potenza aerobica, con blocchi più lunghi rispetto all'Allenamento 2.</p>
  {atletico_svg}
  <div class="three">
    <div class="box"><h4>Organizzazione</h4><ul class="clean">
      <li>2 blocchi da 12 minuti</li>
      <li>5 minuti di recupero tra i blocchi</li>
    </ul></div>
    <div class="box"><h4>Svolgimento</h4>
      <p>In ogni blocco si alterna <b>1 minuto di corsa lenta</b> e <b>30 secondi di corsa veloce</b>, senza fermarsi.</p>
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
    <div class="box"><h4>Prima di andare</h4>Chi ha perso la partita paga i suoi <b>suicidi</b> (vedi Esercitazione II).</div>
  </div>
  {footer()}
</section>'''

html = (testa + "<!-- 1. COPERTINA -->\n" + copertina + "\n\n"
        + "\n\n".join([scheda, partita, ld1, ld2, ld3, gioco, atletico]) + "\n\n</body>\n</html>\n")
(QUI / "allenamento-03.html").write_text(html)
print("pagine:", PAG[0])
