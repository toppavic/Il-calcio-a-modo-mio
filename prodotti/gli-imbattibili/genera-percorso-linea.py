"""Genera percorso-linea-difende-la-palla.html: Dai quaderni del mister · Percorso 2 · La linea che difende la palla.

Contenuti dell'allenatore (29/10/2026) in prodotti/percorsi/linea-difende-la-palla/bozza.md: progressione 2c2 · 2c4 · 4c6 ·
4c8 · 6c8 · 6c10, regole a partita, porta vera e porta mobile, porticine esterne, tempi, ruoli. Titoli delle tappe, obiettivi,
punti di attenzione, errori e criteri di passaggio sono indicazioni editoriali (da far controllare all'allenatore).
Stile e simboli dal Percorso 1 (percorso-ricerca-del-portiere.html).
Uso: python3 genera-percorso-linea.py  poi  render.js sul file .html
"""
import pathlib

QUI = pathlib.Path(__file__).parent
p1 = (QUI / "percorso-ricerca-del-portiere.html").read_text()
PIEDE = "Percorso 2 · La linea che difende la palla"

testa = p1[: p1.index('<section class="page cop">')]
testa = testa.replace("<title>Dai quaderni del mister – La ricerca del portiere</title>",
                      "<title>Dai quaderni del mister – La linea che difende la palla</title>")
testa = testa.replace(".cop { background: #0b1d15;", ".cop { background: #10233a;")
testa = testa.replace("</style>\n</head>", """
.chi { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm; margin-bottom: 3mm; }
.chi div { background: var(--fondo); border-radius: 1.5mm; padding: 2mm 3mm; font-size: 9pt; line-height: 1.4; }
.chi b { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-weight: 500; letter-spacing: .05em; display: block; font-size: 8.5pt; }
.regole2 { display: grid; grid-template-columns: 1.2fr 1fr; gap: 3mm; margin-top: 3mm; }
.regole2 .box { padding: 3mm 4mm; font-size: 9pt; line-height: 1.42; }
.regole2 .box li { margin-bottom: 1mm; }
.copy { font-size: 8pt; color: var(--tenue); margin-top: 4mm; }
</style>
</head>""", 1)

PAG = [0]


def footer():
    PAG[0] += 1
    return (f'<div class="footer"><b>DAI QUADERNI DEL MISTER</b><span>{PIEDE}</span>'
            f'<span>{PAG[0]}</span></div>')


def lista(voci):
    return '<ul class="clean">' + "".join(f"<li>{v}</li>" for v in voci) + "</ul>"


def testo(x, y, t, col="#f2c230", size=11, anchor="middle"):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="Oswald" font-size="{size}" font-weight="700" fill="{col}" '
            f'text-anchor="{anchor}" letter-spacing="1">{t}</text>')


class Campo:
    """Campo in orizzontale: porta vera a destra (la difende la linea), porta mobile a sinistra.
    Coordinate in metri: d = distanza dalla linea di porta vera, y = distanza dalla linea laterale in alto."""

    def __init__(self, L, W, porticine=False):
        self.L, self.W, self.porticine = L, W, porticine
        self.s = min(430 / L, 320 / W)
        self.fl, self.fw = L * self.s, W * self.s
        self.x0, self.y0 = 45, 25
        self.zoom = .255
        self.parti = []
        self.sotto = ""

    def P(self, d, y):
        return self.x0 + self.fl - d * self.s, self.y0 + y * self.s

    def g(self, d, y, sym, n=""):
        x, yy = self.P(d, y)
        t = (f'<text x="{x:.0f}" y="{yy + 4.5:.0f}" font-family="Oswald" font-size="12" font-weight="700" '
             f'text-anchor="middle" fill="#fff">{n}</text>') if n != "" else ""
        self.parti.append(f'<use href="#{sym}" x="{x:.0f}" y="{yy:.0f}"/>{t}')

    def palla(self, d, y):
        x, yy = self.P(d, y)
        self.parti.append(f'<use href="#palla" x="{x + 10:.0f}" y="{yy + 8:.0f}"/>')

    def freccia(self, d1, y1, d2, y2, tipo="movimento"):
        (a, b), (c, e) = self.P(d1, y1), self.P(d2, y2)
        if tipo == "movimento":
            st = 'stroke="#f2c230" stroke-width="2.5" marker-end="url(#freccia-oro)"'
        elif tipo == "conduzione":
            st = 'stroke="#f2c230" stroke-width="2.5" stroke-dasharray="3 4" marker-end="url(#freccia-oro)"'
        else:
            st = 'stroke="#fff" stroke-width="2.5" stroke-dasharray="7 5" marker-end="url(#freccia)"'
        self.parti.append(f'<path d="M{a:.0f},{b:.0f} L{c:.0f},{e:.0f}" fill="none" {st}/>')

    def scritta(self, d, y, t, col="#f2c230", size=11):
        x, yy = self.P(d, y)
        self.parti.append(testo(x, yy, t, col, size))

    def didascalia(self, t):
        self.sotto = t

    def linea_fuorigioco(self, d):
        (a, b), (c, e) = self.P(d, 0), self.P(d, self.W)
        self.parti.append(f'<path d="M{a:.0f},{b:.0f} L{c:.0f},{e:.0f}" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 4" opacity=".7"/>')

    def svg(self, larghezza=None):
        L, W, s = self.L, self.W, self.s
        vw, vh = self.fl + 90, self.fw + (70 if self.sotto else 50)
        X = lambda d: self.x0 + self.fl - d * s
        Y = lambda y: self.y0 + y * s
        c = W / 2
        linee = [f'<rect x="{self.x0}" y="{self.y0}" width="{self.fl:.0f}" height="{self.fw:.0f}"/>']
        for prof, larg in ((16.5, 40.32), (5.5, 18.32)):
            y1, y2 = max(0, c - larg / 2), min(W, c + larg / 2)
            linee.append(f'<path d="M{X(0):.0f},{Y(y1):.0f} L{X(prof):.0f},{Y(y1):.0f} L{X(prof):.0f},{Y(y2):.0f} L{X(0):.0f},{Y(y2):.0f}"/>')
        if L > 30:
            linee.append(f'<circle cx="{X(11):.0f}" cy="{Y(c):.0f}" r="2" fill="#fff"/>')
        porta_v = f'<rect x="{X(0):.0f}" y="{Y(c - 3.66):.0f}" width="12" height="{7.32 * s:.0f}" fill="none" stroke="#fff" stroke-width="3"/>'
        porta_m = f'<rect x="{X(L) - 12:.0f}" y="{Y(c - 2.5):.0f}" width="12" height="{5 * s:.0f}" fill="none" stroke="#fff" stroke-width="3"/>'
        extra = ""
        if self.porticine:
            for y1, y2 in ((0, 6), (W - 6, W)):
                extra += (f'<line x1="{X(L) + 4:.0f}" y1="{Y(y1):.0f}" x2="{X(L) + 4:.0f}" y2="{Y(y2):.0f}" stroke="#f2c230" stroke-width="5" stroke-dasharray="2 {6 * s - 4:.0f}"/>'
                          f'<use href="#pJ" x="{X(L) + 18:.0f}" y="{Y((y1 + y2) / 2):.0f}"/>')
        portieri = (f'<use href="#pP" x="{X(0) + 6:.0f}" y="{Y(c):.0f}"/>'
                    f'<use href="#pP" x="{X(L) - 6:.0f}" y="{Y(c):.0f}"/>')
        lab = (testo(X(0) + 6, Y(c) - 26, "PORTA", "#ffffff", 9) + testo(X(L) - 6, Y(c) - 26, "MOBILE", "#ffffff", 9)
               + testo(self.x0 + self.fl / 2, self.y0 + self.fw + 18, f"{str(L).replace('.', ',')} × {str(W).replace('.', ',')} M", "#ffffff", 10)
               + (testo(self.x0 + self.fl / 2, self.y0 + self.fw + 38, self.sotto, "#f2c230", 11) if self.sotto else ""))
        larghezza = larghezza or f"{min(vw * self.zoom, 150):.0f}mm"
        return f'''<svg class="diagram" viewBox="0 0 {vw:.0f} {vh:.0f}" style="width:{larghezza};margin:0 auto">
    <rect width="{vw:.0f}" height="{vh:.0f}" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">{"".join(linee)}</g>
    {porta_v}{porta_m}{extra}{portieri}{lab}
    {"".join(self.parti)}
  </svg>'''


def tappa(n, formato, titolo, obiettivo, difende, attacca, campo_txt, tempi, schema, regole, cambia, attenzione, errori, passa):
    dopo = f"si passa alla tappa {n + 1} quando" if n < 6 else "il percorso è completato quando"
    return f'''<section class="page">
  <div class="kicker">Tappa {n} di 6 · {formato}</div>
  <div class="ex-title"><h2 style="font-size:20pt">{titolo}</h2></div>
  <div class="campochip">{campo_txt} · <b>{tempi}</b></div>
  <p class="ob"><b>Obiettivo:</b> {obiettivo}</p>
  <div class="chi"><div><b>Chi difende</b>{difende}</div><div><b>Chi attacca</b>{attacca}</div></div>
  {schema}
  <div class="regole2">
    <div class="box"><h4>Regole della tappa</h4>{lista(regole)}</div>
    <div class="box"><h4>Cosa cambia</h4>{lista(cambia)}</div>
  </div>
  <div class="tre" style="grid-template-columns:1.25fr 1fr">
    <div class="box"><h4>Punti di attenzione del mister</h4>{lista(attenzione)}</div>
    <div class="box"><h4>Errori da evitare</h4>{lista(errori)}</div>
  </div>
  <div class="passa"><h4>Obiettivo raggiunto: {dopo}</h4>{lista(passa)}</div>
  {footer()}
</section>'''


# ======================================================================
# COPERTINA
cop_c = Campo(52.5, 68, porticine=True)
for d, y, n in ((20, 14, 2), (20, 28, 5), (20, 40, 6), (20, 54, 3)):
    cop_c.g(d, y, "pB", n)
for d, y in ((32, 6), (26, 28), (26, 40), (32, 62), (40, 22), (40, 46)):
    cop_c.g(d, y, "pA")
cop_c.palla(32, 6)
cop_c.freccia(20, 14, 28, 8)
for y in (28, 40, 54):
    cop_c.freccia(20, y, 21, y - 8)

copertina = f'''<section class="page cop">
  <img class="logo" src="../../materiale/brand/logo-cerchio.png">
  <div style="position:absolute;left:55mm;right:55mm;top:72mm;opacity:.9">{cop_c.svg("100%")}</div>
  <div class="txt">
    <div class="kick">Il calcio a modo mio · Dai quaderni del mister · Percorso 2</div>
    <h1>La linea che<span>difende la palla</span></h1>
    <div class="claim">Si difende la palla, non gli uomini.</div>
    <p class="sub"><b>6 tappe in inferiorità crescente</b>, dal 2 contro 2 al 6 contro 10, sempre a partita: chi segna resta in campo.</p>
  </div>
</section>'''

# ======================================================================
# GUIDA
guida = f'''<section class="page">
  <div class="kicker">Guida al percorso</div>
  <div class="ex-title"><h2>Difendere la palla, non gli uomini</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>Il percorso insegna alla <b>linea a 4</b> a difendere lavorando sulla palla. Si parte dalla coppia, nel 2 contro 2, e si arriva alla linea con i due mediani contro dieci attaccanti. Tappa dopo tappa gli attaccanti crescono più dei difensori: in inferiorità non si può marcare l'uomo, si deve leggere la palla, attaccarla con il giocatore più vicino e coprire con gli altri.</p>
    <p>Ogni tappa si gioca <b>a partita</b>: chi segna resta in campo. È questo che fa la differenza, perché i giocatori diventano molto più aggressivi. E non si allena solo la fase difensiva: chi attacca deve fare gol, dal 2 contro 4 c'è il fuorigioco e chi difende, quando recupera, deve giocare bene il primo pallone.</p>
    <p>I giocatori lavorano <b>sempre nel loro ruolo</b> e le coppie non si mescolano: due esterni, due punte, due centrocampisti, due terzini, due centrali. Così ogni reparto si abitua a lavorare con gli altri.</p>
  </div>
  <div class="principio"><b>Il principio</b>Il più vicino alla palla la attacca, l'altro dà la copertura. Con la palla scoperta la linea protegge la profondità, con la palla coperta accorcia.</div>
  <h3 style="margin-top:6mm">Come leggere gli schemi</h3>
  <div class="legenda">
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#2a5db0" stroke="#fff" stroke-width="2"/></svg> Difensori (numerati), difendono la porta a destra</div>
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#c8372d" stroke="#fff" stroke-width="2"/></svg> Attaccanti, attaccano verso destra</div>
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#f2c230" stroke="#1d2421" stroke-width="2"/></svg> Portieri: porta vera e porta mobile</div>
    <div><svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="#fff" stroke="#1d2421" stroke-width="2"/></svg> Giocatori di riferimento nelle porticine</div>
    <div><svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg> Movimento</div>
    <div><svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3" stroke-dasharray="3 3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg> Conduzione palla</div>
  </div>
  <p class="nota" style="margin-top:5mm">Esercitazioni, regole, campi e tempi vengono dai quaderni del mister. Titoli delle tappe, obiettivi, punti di attenzione, errori e criteri di passaggio sono indicazioni editoriali per aiutare a usarle.</p>
  {footer()}
</section>'''

regole = f'''<section class="page">
  <div class="kicker">Organizzazione</div>
  <div class="ex-title"><h2>Le regole che non cambiano</h2></div>
  <h3 style="margin-top:4mm">Il campo e le porte</h3>
  <div class="elenco">{lista([
      "La linea difende la <b>porta vera</b>, con il portiere. Di fronte, fuori dall'area, c'è la <b>porta mobile</b> con il suo portiere.",
      "Dal 4 contro 6 si aggiungono due <b>porticine esterne</b> larghe 6 m, all'altezza della porta mobile, ricavate rientrando dalla linea laterale. In ognuna c'è un giocatore di riferimento.",
      "Il campo cresce con il numero dei giocatori: nel 2 contro 2 è largo quanto l'area piccola e lungo 24 m; dal 4 contro 6 è tutta la metà campo."])}</div>
  <h3 style="margin-top:5mm">A partita</h3>
  <div class="elenco">{lista([
      "Si parte <b>sempre dagli attaccanti</b>, con la palla che arriva dalla porta mobile. Gli attaccanti partono dalla porta mobile, i difensori aspettano il turno dietro la porta vera.",
      "L'attacco deve <b>sempre fare gol</b> nella porta vera.",
      "<b>Chi segna resta in campo.</b> Se la palla esce, si cambiano tutti.",
      "Chi difende, quando recupera palla, può usare il proprio portiere <b>al massimo una volta</b> nella stessa azione: deve far viaggiare il pallone, non perdere tempo.",
      "Dal 2 contro 4 vale il <b>fuorigioco</b>."])}</div>
  <h3 style="margin-top:5mm">Quando la difesa recupera palla</h3>
  <table class="tab compatta">
    <tr><th>Tappe</th><th>Che cosa deve fare</th></tr>
    <tr><td class="m">2 contro 2 · 2 contro 4</td><td>Fare gol nella porta mobile.</td></tr>
    <tr><td class="m">4 contro 6 · 4 contro 8</td><td>Trovare il portiere della porta mobile o il giocatore in una porticina, senza tirare: conta la qualità del passaggio.</td></tr>
    <tr><td class="m">6 contro 8 · 6 contro 10</td><td>Attraversare una porticina palla al piede, senza tirare.</td></tr>
  </table>
  <h3 style="margin-top:5mm">I ruoli</h3>
  <div class="elenco">{lista([
      "Ognuno gioca nel suo ruolo e le coppie non si mescolano: mai una punta con un centrocampista.",
      "Nel 2 contro 2 e nel 2 contro 4 le coppie che difendono girano: terzino e centrale, i due centrali, centrale e terzino.",
      "L'ideale è avere almeno 20 giocatori; con meno, anche 16, si adatta il numero senza spostare i giocatori dal loro ruolo."])}</div>
  {footer()}
</section>'''

QUADRO = [
    ("2 contro 2", "Coppia: terzino e centrale, i due centrali, centrale e terzino", "Due attaccanti", "18 × 24 m", "4 × 1'30\""),
    ("2 contro 4", "Coppia, a rotazione", "Due esterni + due punte o due centrocampisti", "30 × 24 m", "4 × 1'30\""),
    ("4 contro 6", "Linea 2-5-6-3", "Punte, esterni, centrocampisti", "Metà campo", "4 × 5'"),
    ("4 contro 8", "Linea 2-5-6-3", "+ i due terzini", "Metà campo", "4 × 5'"),
    ("6 contro 8", "Linea + mediani 4 e 8", "Punte, esterni, centrocampisti, terzini", "Metà campo", "4 × 5'"),
    ("6 contro 10", "Linea + mediani 4 e 8", "+ i due centrali", "Metà campo", "4 × 5'"),
]
righe = "".join(f'<tr><td class="n">{i}</td><td class="m">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td style="white-space:nowrap">{e}</td></tr>'
                for i, (a, b, c, d, e) in enumerate(QUADRO, 1))
NOTE_TEMPI = lista([
      "<b>2 contro 2 e 2 contro 4:</b> 4 tempi da 1'30\" con 30-40\" di recupero.",
      "<b>Dal 4 contro 6:</b> 4 tempi da 5' con 1'30\" di recupero, per non perdere tempo. Se nella seduta c'è già stato un lavoro fisico importante, tempi da 3': è un lavoro molto impegnativo.",
      "Metà campo: 52,5 × 68 m su un campo regolamentare."])
quadro = f'''<section class="page">
  <div class="kicker">La progressione</div>
  <div class="ex-title"><h2>Il quadro delle 6 tappe</h2></div>
  <table class="tab" style="margin-top:5mm">
    <tr><th></th><th>Formato</th><th>Chi difende</th><th>Chi attacca</th><th>Campo</th><th>Tempi</th></tr>
    {righe}
  </table>
  <div class="elenco" style="margin-top:5mm">{NOTE_TEMPI}</div>
  <div class="principio" style="margin-top:6mm"><b>Lettura della progressione</b>Nelle prime due tappe la coppia impara ad attaccare la palla e a coprire, prima alla pari e poi in inferiorità. Dalla terza la linea a 4 scivola insieme e protegge la profondità contro avversari sempre più numerosi. Nelle ultime due i mediani lavorano davanti alla linea: la difesa diventa un blocco di sei che difende la palla contro otto e poi dieci.</div>
  {footer()}
</section>'''

# ======================================================================
# LE 6 TAPPE
c1 = Campo(24, 18.32)
c1.zoom = .22
c1.g(10, 5, "pB", 2); c1.g(10, 13, "pB", 5)
c1.g(19, 5, "pA"); c1.g(17, 13, "pA"); c1.palla(19, 5)
c1.freccia(10, 5, 16.5, 5); c1.freccia(10, 13, 12, 8.5)
c1.scritta(13, 2.2, "ATTACCA LA PALLA", size=10); c1.scritta(8.5, 16.5, "COPRE", size=10)
t1 = tappa(1, "2 contro 2", "Chi attacca la palla, chi copre",
    "la coppia impara ad accorciare subito sul portatore e a dividersi i compiti: il più vicino attacca la palla, l'altro dà la copertura.",
    "Una coppia: terzino e centrale, i due centrali, centrale e terzino, a rotazione.", "Due attaccanti, con la palla.",
    "18 × 24 m: larghezza dell'area piccola, 24 m di lunghezza", "4 tempi da 1'30\" · recupero 30-40\"", c1.svg(),
    ["Difensori in fila dietro la porta vera, attaccanti alla porta mobile.", "Si parte sempre dall'attacco, con la palla.",
     "Chi segna resta in campo; se la palla esce si cambiano tutti e quattro.", "La coppia che recupera deve fare gol nella porta mobile; il proprio portiere si usa al massimo una volta."],
    ["È la base del percorso: si gioca alla pari.", "Chi porta palla parte fuori dal limite dell'area: se nessuno accorcia, tira subito."],
    ["Il difensore più vicino scatta ad accorciare prima che il portatore alzi la testa.", "Il compagno si mette in copertura dietro e di lato, non in linea.", "Dopo il recupero si attacca subito la porta mobile."],
    ["Aspettare il portatore dentro l'area.", "Uscire in due sullo stesso attaccante.", "Usare il portiere per perdere tempo."],
    ["La coppia accorcia sempre sul portatore e i tiri da fuori area diminuiscono.", "Chi copre si trova al posto giusto senza indicazioni.", "Le coppie che recuperano palla segnano nella porta mobile."])

c2 = Campo(24, 30)
c2.g(10, 11, "pB", 2); c2.g(10, 19, "pB", 5)
c2.g(17, 4, "pA"); c2.g(17, 26, "pA"); c2.g(14, 12, "pA"); c2.g(14, 18, "pA"); c2.palla(17, 4)
c2.freccia(10, 11, 15, 6); c2.freccia(10, 19, 11, 13.5)
c2.linea_fuorigioco(9.2); c2.scritta(8.2, 29, "FUORIGIOCO", "#ffffff", 9)
t2 = tappa(2, "2 contro 4", "La coppia in inferiorità",
    "in due contro quattro non si può marcare l'uomo: la coppia sceglie la palla, la attacca con il più vicino e copre lo spazio più pericoloso.",
    "Una coppia, a rotazione come nel 2 contro 2.", "Una coppia di esterni con le due punte o con i due centrocampisti: le coppie non si mescolano.",
    "30 × 24 m: più largo, stessa lunghezza", "4 tempi da 1'30\" · recupero 30-40\"", c2.svg(),
    ["Le regole del 2 contro 2.", "Comincia il fuorigioco.", "La coppia che recupera deve fare gol nella porta mobile, a 24 m."],
    ["Gli attaccanti diventano quattro e il campo si allarga.", "Con il fuorigioco la coppia può salire e togliere spazio alle spalle."],
    ["Si attacca la palla, non l'attaccante più vicino.", "Chi copre si stringe verso il centro e la porta.", "La coppia sale insieme per mettere in fuorigioco."],
    ["Inseguire gli uomini senza palla.", "Un difensore che sale e l'altro che resta.", "Lasciare il portatore libero di tirare."],
    ["La coppia attacca la palla e copre anche in inferiorità.", "Gli attaccanti finiscono spesso in fuorigioco.", "I gol subiti arrivano più da azioni lunghe che da tiri immediati."])

def base4(c):
    for d, y, n in ((20, 14, 2), (20, 28, 5), (20, 40, 6), (20, 54, 3)):
        c.g(d, y, "pB", n)

c3 = Campo(52.5, 68, porticine=True)
base4(c3)
for d, y in ((32, 6), (32, 62), (26, 28), (26, 40), (40, 22), (40, 46)):
    c3.g(d, y, "pA")
c3.palla(32, 6)
c3.freccia(20, 14, 28.5, 8.5)
for y in (28, 40, 54):
    c3.freccia(20, y, 20, y - 7)
c3.didascalia("LA LINEA SCIVOLA VERSO LA PALLA")
t3 = tappa(3, "4 contro 6", "La linea scivola con la palla",
    "la linea a 4 si muove insieme in base alla posizione della palla: il più vicino esce, gli altri scivolano e coprono.",
    "La linea 2-5-6-3.", "Le due punte, i due esterni e i due centrocampisti.",
    "Tutta la metà campo, 52,5 × 68 m", "4 tempi da 5' · recupero 1'30\"", c3.svg(),
    ["Le regole a partita, con il fuorigioco.", "La difesa che recupera trova il portiere della porta mobile o il giocatore in una porticina, senza tirare."],
    ["Si passa alla linea intera e alla metà campo.", "Compaiono le porticine esterne all'altezza della porta mobile."],
    ["Il terzino lato palla esce sull'esterno, i compagni scivolano e restano compatti.", "Distanze costanti tra i quattro.", "Dopo il recupero il primo passaggio è preciso, sul portiere o sul riferimento."],
    ["Scivolare uno alla volta.", "Lasciare buchi tra centrale e terzino.", "Calciare via il pallone dopo il recupero."],
    ["La linea si muove compatta senza indicazioni.", "Le uscite hanno sempre la copertura.", "I recuperi diventano passaggi giusti verso il portiere o le porticine."])

c4 = Campo(52.5, 68, porticine=True)
for d, y, n in ((20, 14, 2), (20, 28, 5), (20, 40, 6), (20, 54, 3)):
    c4.g(d, y, "pB", n)
for d, y in ((32, 6), (32, 62), (26, 28), (26, 40), (40, 22), (40, 46), (46, 12), (46, 56)):
    c4.g(d, y, "pA")
c4.palla(40, 22)
for y in (14, 28, 40, 54):
    c4.freccia(20, y, 15, y)
c4.didascalia("PALLA SCOPERTA · LA LINEA PROTEGGE LA PROFONDITÀ")
t4 = tappa(4, "4 contro 8", "Proteggere la profondità",
    "contro otto attaccanti la linea legge la palla: quando il portatore è libero di giocare in profondità la linea scappa insieme, quando è pressato accorcia.",
    "La linea 2-5-6-3.", "Punte, esterni, centrocampisti e i due terzini.",
    "Tutta la metà campo, 52,5 × 68 m", "4 tempi da 5' · recupero 1'30\"", c4.svg(),
    ["Le regole a partita, con il fuorigioco.", "La difesa che recupera trova il portiere della porta mobile o il giocatore in una porticina, senza tirare."],
    ["Entrano i due terzini: gli attaccanti diventano otto.", "La linea deve scegliere quando proteggere la profondità e quando salire."],
    ["Con la palla scoperta la linea arretra insieme, prima che parta il passaggio.", "Con la palla coperta la linea accorcia e usa il fuorigioco.", "Il più vicino attacca la palla solo se i compagni coprono."],
    ["Uscire sulla palla lasciando la profondità scoperta.", "Un difensore disallineato che tiene in gioco tutti.", "Inseguire i terzini che si sovrappongono."],
    ["La linea arretra e sale insieme, in base alla palla.", "I passaggi alle spalle della linea diminuiscono.", "Il fuorigioco è usato con i tempi giusti."])

c5 = Campo(52.5, 68, porticine=True)
for d, y, n in ((22, 14, 2), (22, 28, 5), (22, 40, 6), (22, 54, 3), (30, 26, 4), (30, 42, 8)):
    c5.g(d, y, "pB", n)
for d, y in ((32, 6), (32, 62), (26, 34), (40, 20), (40, 46), (46, 12), (46, 56), (28, 50)):
    c5.g(d, y, "pA")
c5.palla(40, 20)
c5.freccia(30, 26, 37, 21.5)
for y in (14, 28, 40, 54):
    c5.freccia(22, y, 26, y)
c5.didascalia("PALLA COPERTA · LA LINEA ACCORCIA")
t5 = tappa(5, "6 contro 8", "I mediani davanti alla linea",
    "i due mediani lavorano con la linea: attaccano la palla davanti alla difesa e, quando la palla è coperta, la linea accorcia per stringere gli spazi.",
    "La linea 2-5-6-3 con i mediani 4 e 8.", "Punte, esterni, centrocampisti e terzini.",
    "Tutta la metà campo, 52,5 × 68 m", "4 tempi da 5' · recupero 1'30\"", c5.svg(),
    ["Le regole a partita, con il fuorigioco.", "La difesa che recupera deve attraversare una porticina palla al piede, senza tirare."],
    ["Entrano i mediani: la difesa diventa un blocco di sei.", "Dopo il recupero non basta passare: si esce palla al piede."],
    ["Il mediano più vicino attacca la palla, l'altro chiude la linea centrale.", "Quando il mediano copre la palla, la linea accorcia insieme.", "Dopo il recupero si porta palla verso la porticina libera."],
    ["Mediani schiacciati sulla linea.", "Linea che resta bassa con la palla coperta.", "Uscire dal recupero con un passaggio forzato."],
    ["Mediani e linea si muovono come un solo reparto.", "Le palle coperte diventano recuperi.", "I recuperi diventano uscite palla al piede."])

c6 = Campo(52.5, 68, porticine=True)
for d, y, n in ((22, 14, 2), (22, 28, 5), (24, 40, 6), (22, 54, 3), (30, 26, 4), (30, 42, 8)):
    c6.g(d, y, "pB", n)
for d, y in ((32, 6), (32, 62), (26, 34), (40, 20), (40, 46), (46, 12), (46, 56), (28, 50), (44, 30), (44, 38)):
    c6.g(d, y, "pA")
c6.palla(24, 40)
c6.freccia(24, 42, 50, 63, "conduzione")
c6.didascalia("RECUPERO · SI ATTRAVERSA LA PORTICINA")
t6 = tappa(6, "6 contro 10", "Tutto insieme contro dieci",
    "il blocco di sei difende la palla contro dieci attaccanti, mettendo insieme tutto il percorso: attacco e copertura, scivolamento, profondità, mediani davanti alla linea.",
    "La linea 2-5-6-3 con i mediani 4 e 8.", "Punte, esterni, centrocampisti, terzini e i due centrali.",
    "Tutta la metà campo, 52,5 × 68 m", "4 tempi da 5' · recupero 1'30\" (3' dopo un lavoro fisico pesante)", c6.svg(),
    ["Le regole a partita, con il fuorigioco.", "La difesa che recupera deve attraversare una porticina palla al piede, senza tirare."],
    ["Entrano i due centrali: gli attaccanti diventano dieci.", "Nessuna regola nuova: si verifica se il blocco difende da solo."],
    ["Si difende la palla anche quando gli uomini liberi sono tanti.", "Ogni uscita ha la sua copertura.", "La linea sceglie da sola quando proteggere la profondità e quando accorciare."],
    ["Andare a marcare l'uomo libero lontano dalla palla.", "Perdere la distanza tra mediani e linea.", "Correggere ogni azione dalla panchina."],
    ["Il blocco di sei si muove sulla palla senza indicazioni.", "I gol subiti arrivano solo dopo azioni lunghe.", "Se un comportamento manca, si torna alla tappa che lo allena."])

nota = f'''<section class="page">
  <div class="kicker">Prima di usarlo</div>
  <div class="ex-title"><h2>Non avere fretta</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>Il percorso non va affrontato con la fretta di arrivare al 6 contro 10. Ogni tappa va assimilata prima di passare alla successiva: si va avanti quando i comportamenti indicati in fondo alla pagina si vedono con regolarità, senza continue indicazioni dell'allenatore. Se non succede, si ripropone la stessa tappa nelle sedute successive.</p>
    <p>Il lavoro è molto impegnativo dal punto di vista fisico: con tempi da 5' e recuperi brevi l'intensità resta alta. Se nella seduta c'è già stato un lavoro fisico importante, meglio passare ai tempi da 3'.</p>
    <p>Il numero ideale è almeno 20 giocatori, ma il percorso si adatta anche a 16: si cambia il numero dei gruppi, non il ruolo dei giocatori.</p>
  </div>
  <p class="copy">© Il calcio a modo mio · Dai quaderni del mister. Materiale per uso personale: è vietata la diffusione, la copia e la rivendita.</p>
  {footer()}
</section>'''

pagine = [copertina, guida, regole, quadro, t1, t2, t3, t4, t5, t6, nota]
html = testa + "\n\n".join(pagine) + "\n\n</body>\n</html>\n"
(QUI / "percorso-linea-difende-la-palla.html").write_text(html)
print("pagine:", len(pagine))
