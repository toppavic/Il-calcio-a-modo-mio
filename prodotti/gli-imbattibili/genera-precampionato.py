"""Genera precampionato-allenamenti-1-10.html: il pacchetto da vendere con i primi 10 allenamenti.

Copertina del pacchetto + "Prima di cominciare" + indice, poi le pagine dei 10 allenamenti
così come sono (ognuno con la sua copertina, che fa da separatore).
Uso: python3 genera-precampionato.py  poi  render.js sul file .html
"""
import pathlib
import re

QUI = pathlib.Path(__file__).parent
N = range(1, 11)
html = {i: (QUI / f"allenamento-{i:02d}.html").read_text() for i in N}

# Stili e simboli SVG: l'Allenamento 10 contiene quelli di tutti gli altri
testa = html[10][: html[10].index("<!-- 1. COPERTINA -->")]
testa = testa.replace("<title>Gli Imbattibili – Precampionato, Allenamento 10</title>",
                      "<title>Gli Imbattibili – Il Precampionato, Allenamenti 1-10</title>")
testa = testa.replace("</style>\n</head>", """.indice { width: 100%; border-collapse: collapse; margin-top: 4mm; }
.indice td { padding: 3.2mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 10.5pt; vertical-align: middle; }
.indice .n { font-family: Oswald, sans-serif; font-size: 20pt; color: var(--oro); width: 14mm; }
.indice .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 13pt; letter-spacing: .02em; }
.indice .d { color: #5d6b65; font-size: 9.5pt; }
.indice .p { font-family: Oswald, sans-serif; color: var(--verde); font-size: 13pt; text-align: right; width: 16mm; }
.legenda { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm 6mm; margin-top: 3mm; font-size: 10pt; }
.legenda div { display: flex; align-items: center; gap: 3mm; }
.legenda svg { flex: none; }
.testo p { font-size: 11pt; line-height: 1.6; margin-bottom: 3mm; }
</style>
</head>""", 1)


def corpo(i):
    h = html[i]
    return h[h.index("<!-- 1. COPERTINA -->"): h.index("</body>")].strip()


def campo(h, etichetta):
    m = re.search(rf'<div class="l">{etichetta}</div><div class="v">(.*?)</div>', h)
    return m.group(1) if m else ""


def pagine(i):
    return html[i].count('<section class="page')


# ---------- Copertina del pacchetto (stessa grafica delle copertine degli allenamenti)
copertina = re.search(r'<section class="page c5">.*?</section>', html[1], re.S).group(0)
copertina = (copertina
             .replace("allenamento-01.jpg", "allenamento-05.jpg")
             .replace("Precampionato · Allenamento 1", "Il precampionato · Allenamenti 1-10")
             .replace("la prima seduta della Juniores", "le prime dieci sedute del precampionato della Juniores"))

FOOT = '<div class="footer"><b>GLI IMBATTIBILI</b><span>Il precampionato · Allenamenti 1-10</span><span>{}</span></div>'

# ---------- Prima di cominciare
def pallino(colore, bordo="#fff", testo=""):
    t = f'<text x="13" y="17.5" font-family="Oswald" font-size="12" font-weight="700" text-anchor="middle" fill="#fff">{testo}</text>' if testo else ""
    return f'<svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="{colore}" stroke="{bordo}" stroke-width="2"/>{t}</svg>'

freccia_oro = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg>'
passaggio = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#5d6b65" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M28,2 L38,7 L28,12 Z" fill="#5d6b65"/></svg>'

intro = f'''<section class="page">
  <div class="kicker">Il precampionato</div>
  <div class="ex-title"><h2>Prima di cominciare</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>Questi sono gli allenamenti veri del precampionato della <b>Juniores provinciale che ha poi vinto il campionato senza perdere una partita</b>. Sono trascritti dai quaderni dell'allenatore, seduta per seduta, così come sono stati fatti in campo.</p>
    <p>Per ogni allenamento trovi la <b>scheda della seduta</b> (durata, programma e barra dei tempi) e una pagina per ogni esercitazione con <b>obiettivo, schema, organizzazione, svolgimento e punti chiave</b>. Le partite a tema hanno le regole tempo per tempo: tocchi, vincoli e punteggi.</p>
    <p>La squadra gioca con il <b>4-2-3-1</b>. La linea difensiva, guardando lo schema con la porta in alto, è sempre <b>2-5-6-3</b> da sinistra a destra.</p>
  </div>

  <h3 style="margin-top:6mm">Come leggere gli schemi</h3>
  <div class="legenda">
    <div>{pallino("#2a5db0", testo="5")} Difensori e squadra di riferimento (numerati)</div>
    <div>{pallino("#c8372d")} Attaccanti e avversari</div>
    <div>{pallino("#f2c230", "#1d2421")} Portiere</div>
    <div>{pallino("#ffffff", "#1d2421")} Jolly</div>
    <div>{freccia_oro} Movimento del giocatore</div>
    <div>{passaggio} Passaggio, lancio o cross</div>
  </div>

  <div class="chiave" style="margin-top:9mm">
    <span class="kicker">Il libro</span>
    La stagione di questa squadra è raccontata nel libro <b>“Gli Imbattibili”</b>, su Amazon. Il libro racconta cosa è successo. Questi allenamenti mostrano come ci siamo arrivati.
  </div>
  {FOOT.format(2)}
</section>'''

# ---------- Indice
righe, pag = [], 4
for i in N:
    durata, focus = campo(html[i], "Durata"), campo(html[i], "Focus")
    righe.append(f'<tr><td class="n">{i}</td><td><div class="t">Allenamento {i}</div>'
                 f'<div class="d">{focus} · {durata}</div></td><td class="p">p. {pag}</td></tr>')
    pag += pagine(i)

indice = f'''<section class="page">
  <div class="kicker">Il precampionato</div>
  <div class="ex-title"><h2>Indice</h2></div>
  <table class="indice">{"".join(righe)}</table>
  {FOOT.format(3)}
</section>'''

# Copertine come immagini (se già create con strumenti/render-copertine.js): il PDF resta sotto i 20 MB di Etsy
COP = QUI / "copertine-pacchetto"
if COP.exists():
    sezioni = iter(range(100))
    def a_immagine(m):
        n = next(sezioni)
        return (f'<section class="page" style="padding:0"><img src="copertine-pacchetto/copertina-{n:02d}.jpg" '
                'style="width:100%;height:100%;display:block"></section>')
    copertina = re.sub(r'<section class="page c5">.*?</section>', a_immagine, copertina, flags=re.S)
    corpi = [re.sub(r'<section class="page c5">.*?</section>', a_immagine, corpo(i), flags=re.S) for i in N]
else:
    corpi = [corpo(i) for i in N]

out = (testa + "<!-- COPERTINA DEL PACCHETTO -->\n" + copertina + "\n\n" + intro + "\n\n" + indice + "\n\n"
       + "\n\n".join(f"<!-- ===== ALLENAMENTO {i} ===== -->\n" + c for i, c in zip(N, corpi))
       + "\n\n</body>\n</html>\n")
(QUI / "precampionato-allenamenti-1-10.html").write_text(out)
print("pagine:", pag - 1)
