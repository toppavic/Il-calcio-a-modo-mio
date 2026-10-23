"""Genera campionato-allenamenti-11-19.html: il pacchetto "In campionato" con gli Allenamenti 11-19.

Revisione del 23/10/2026: una sola copertina, per ogni allenamento la pagina con la foto del foglio
originale (data, precisazioni dell'autore, adattamenti consigliati), le pagine dell'allenamento,
una pagina di indicazioni tecniche dopo ogni esercitazione principale e, dopo le partite,
cosa osservare in campo. Numerazione continua e indice calcolato sulle pagine vere.
Contenuti editoriali in campionato_editoriale.py.
Uso: prima gli script genera-allenamento-11…19.py, poi python3 genera-campionato.py e render.js sul file .html
"""
import pathlib
import re

from campionato_editoriale import FONTI, PARTITE, TECNICHE

QUI = pathlib.Path(__file__).parent
N = range(11, 20)
html = {i: (QUI / f"allenamento-{i:02d}.html").read_text() for i in N}
SEZ = re.compile(r'<section class="page[^"]*">.*?</section>', re.S)

# Stili e simboli SVG: l'Allenamento 19 contiene quelli usati in campionato (stazioni, tabellone, statistiche)
testa = html[19][: html[19].index("<!-- 1. COPERTINA -->")]
testa = re.sub(r"<title>.*?</title>", "<title>Gli Imbattibili – In campionato, Allenamenti 11-19</title>", testa)
extra11 = html[11][html[11].index(".intervalli {"): html[11].index("</style>")]
testa = testa.replace("</style>\n</head>", extra11 + """
.indice { width: 100%; border-collapse: collapse; margin-top: 4mm; }
.indice td { padding: 3mm 2mm; border-bottom: 1px solid #e3e8e5; font-size: 10.5pt; vertical-align: middle; }
.indice .n { font-family: Oswald, sans-serif; font-size: 20pt; color: var(--oro); width: 14mm; }
.indice .t { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 13pt; letter-spacing: .02em; }
.indice .d { color: #5d6b65; font-size: 9.8pt; }
.indice .p { font-family: Oswald, sans-serif; color: var(--verde); font-size: 13pt; text-align: right; width: 16mm; }
.legenda { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm 6mm; margin-top: 3mm; font-size: 10pt; }
.legenda div { display: flex; align-items: center; gap: 3mm; }
.legenda svg { flex: none; }
.testo p { font-size: 11pt; line-height: 1.6; margin-bottom: 3mm; }
/* leggibilità su smartphone: riquadri su una riga ciascuno, testo più grande */
.three { grid-template-columns: 1fr !important; gap: 2mm !important; margin-top: 4mm !important; }
.three .box { display: grid; grid-template-columns: 33mm 1fr; gap: 4mm; font-size: 10pt !important; padding: 2.6mm 4mm; }
.three .box h4 { margin: 0; font-size: 10.5pt; }
.three .box p { margin-bottom: 1mm !important; }
.three .box p:last-child { margin-bottom: 0 !important; }
.three .box ul.clean li { margin-bottom: .6mm; }
.chip { font-size: 8.8pt !important; }
.obj { font-size: 10.5pt; }
/* livelli delle fonti */
.liv { display: inline-block; font-family: Oswald, sans-serif; font-size: 8.5pt; letter-spacing: .08em; text-transform: uppercase; padding: .6mm 2.4mm; border-radius: 1mm; margin-right: 2mm; vertical-align: 1px; }
.liv.q { background: var(--verde); color: #fff; }
.liv.a { background: var(--oro); color: var(--verde); }
.liv.c { background: #e6efe9; color: var(--verde); border: 1px solid #b9cdc2; }
.foglio { display: block; margin: 3mm auto 0; max-height: 150mm; max-width: 100%; border: 1px solid #dfe5e1; border-radius: 1.5mm; box-shadow: 0 1mm 3mm rgba(0,0,0,.08); }
.fonti { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; margin-top: 4mm; }
.fonti .box { font-size: 9.8pt; line-height: 1.45; padding: 3mm 4mm; }
.fonti .box li { margin-bottom: 1mm; }
.nota-f { margin-top: 3mm; font-size: 9.6pt; background: #fbf6e6; border-left: 4px solid var(--oro); padding: 2.2mm 3.5mm; border-radius: 0 1.5mm 1.5mm 0; }
.tec h3 { font-size: 11pt; margin: 4mm 0 1.5mm; }
.tec .riga { display: grid; grid-template-columns: 30mm 1fr; gap: 4mm; padding: 2.2mm 0; border-bottom: 1px solid #e3e8e5; font-size: 10.2pt; }
.tec .riga .l { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 10pt; letter-spacing: .04em; }
.tec .ob { font-size: 11pt; line-height: 1.55; margin: 3mm 0 2mm; }
.tec .liste { display: grid; grid-template-columns: 1fr; gap: 3mm; margin-top: 3mm; }
.tec .liste .box { font-size: 10.2pt; line-height: 1.45; padding: 3mm 4.5mm; }
.tec .liste .box li { margin-bottom: 1mm; }
.osserva { margin-top: 4mm; font-size: 9.8pt; background: #edf4ef; border-left: 4px solid var(--verde); padding: 2.5mm 4mm; border-radius: 0 1.5mm 1.5mm 0; }
.osserva h4 { font-family: Oswald, sans-serif; text-transform: uppercase; color: var(--verde); font-size: 10.5pt; letter-spacing: .04em; margin-bottom: 1mm; }
.osserva .nb { color: var(--tenue); font-size: 8.8pt; margin-top: 1mm; }
</style>
</head>""", 1)


def lista(voci):
    return '<ul class="clean">' + "".join(f"<li>{v}</li>" for v in voci) + "</ul>"


def piede(i):
    fase = "Precampionato" if i == 11 else "In campionato"
    return f'<div class="footer"><b>GLI IMBATTIBILI</b><span>{fase} · Allenamento {i}</span><span>#</span></div>'


# ---------- Pagina del foglio originale (al posto della copertina di ogni allenamento)
def pagina_foglio(i):
    f = FONTI[i]
    data = f" · {f['data']}" if f["data"] else " · data non indicata sul foglio"
    autore = (lista(f["autore"]) if f["autore"] else "<p>Nessuna precisazione: la seduta è trascritta così come è sul foglio.</p>")
    fisico = ('<div class="nota-f"><b>Lavoro fisico</b> (rapidità, corsa, navette, suicidi, flessioni): è la documentazione di '
              "quanto svolto con questa squadra, non una prescrizione. Chi lo riusa lo adatta al proprio gruppo.</div>") if f["fisico"] else ""
    return f'''<section class="page">
  <div class="kicker">{f["giorno"]}{data}</div>
  <div class="ex-title"><h2>Allenamento {i} · il foglio originale</h2></div>
  <img class="foglio" src="../../materiale/{f["foto"]}">
  <div class="fonti">
    <div class="box"><h4><span class="liv a">Precisato dall'autore</span></h4>{autore}</div>
    <div class="box"><h4><span class="liv c">Consigliato</span></h4>{lista(f["consigliato"])}</div>
  </div>
  {fisico}
  {piede(i)}
</section>'''


# ---------- Pagina di indicazioni tecniche
def pagina_tecnica(i, t):
    return f'''<section class="page tec">
  <div class="kicker">Allenamento {i} · Indicazioni tecniche · <span style="color:var(--tenue)">aggiunta editoriale, non presente nel quaderno</span></div>
  <div class="ex-title"><h2>{t["titolo"]}</h2></div>
  <p class="ob"><span class="liv c">Consigliato</span><b>Obiettivo tecnico-tattico.</b> {t["obiettivo"]}</p>
  <div class="riga"><div class="l">Tempi</div><div>{t["tempi"]}</div></div>
  <div class="riga"><div class="l">Campo</div><div>{t["campo"]}</div></div>
  <div class="liste">
    <div class="box"><h4>Punti di attenzione del mister</h4>{lista(t["attenzione"])}</div>
    <div class="box"><h4>Errori da evitare</h4>{lista(t["errori"])}</div>
    <div class="box"><h4>Comportamenti osservabili</h4>{lista(t["osservabili"])}</div>
  </div>
  {piede(i)}
</section>'''


def osserva(i):
    return ('<div class="osserva"><h4>Cosa osservare in partita</h4>' + lista(PARTITE[i])
            + '<div class="nb"><span class="liv c">Consigliato</span>Osservazioni editoriali sui principi allenati in settimana: '
              "indicano cosa guardare, non dimostrano che il risultato dipenda dagli allenamenti. Risultato e statistiche sono quelli originali.</div></div>")


def pagine_allenamento(i):
    sez = SEZ.findall(html[i])
    out = [pagina_foglio(i)]
    for k, s in enumerate(sez[1:], 1):  # la copertina (sezione 0) è sostituita dalla pagina del foglio
        if i == 11 and k == 2:
            s = s.replace('<div class="stazioni">', '<div class="stazioni" style="grid-template-columns:1fr 1fr">')
        if i == 11 and k == 3:  # schema più piccolo per far stare partita libera e suicidi nella pagina
            s = s.replace('viewBox="0 0 500 380" style="width:112mm', 'viewBox="0 0 500 380" style="width:84mm')
        if "<h2>La partita</h2>" in s:
            s = s.replace('  <div class="footer">', osserva(i) + '\n  <div class="footer">', 1)
        # nei riquadri della riga il titolo sta a sinistra e il contenuto a destra
        s = re.sub(r'(<div class="box"><h4>(?:Organizzazione|Svolgimento|Punti chiave)</h4>)(.*?)(</div>)',
                   r'\1<div>\2</div>\3', s, flags=re.S)
        s = re.sub(r'(<div class="footer">.*?<span>)\d+(</span></div>)', r"\1#\2", s)
        out.append(s)
        if (i, k) in TECNICHE:
            out.append(pagina_tecnica(i, TECNICHE[(i, k)]))
    return out


# ---------- Copertina del pacchetto (immagine già pronta, sotto i 20 MB di Etsy)
copertina = ('<section class="page" style="padding:0"><img src="copertine-campionato/copertina-00.jpg" '
             'style="width:100%;height:100%;display:block"></section>')

FOOT = '<div class="footer"><b>GLI IMBATTIBILI</b><span>In campionato · Allenamenti 11-19</span><span>#</span></div>'


def pallino(colore, bordo="#fff", testo=""):
    t = f'<text x="13" y="17.5" font-family="Oswald" font-size="12" font-weight="700" text-anchor="middle" fill="#fff">{testo}</text>' if testo else ""
    return f'<svg width="26" height="26"><circle cx="13" cy="13" r="10" fill="{colore}" stroke="{bordo}" stroke-width="2"/>{t}</svg>'


freccia_oro = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#d4a017" stroke-width="3"/><path d="M28,2 L38,7 L28,12 Z" fill="#d4a017"/></svg>'
passaggio = '<svg width="40" height="14"><path d="M2,7 L30,7" stroke="#5d6b65" stroke-width="2.5" stroke-dasharray="6 4"/><path d="M28,2 L38,7 L28,12 Z" fill="#5d6b65"/></svg>'

intro = f'''<section class="page">
  <div class="kicker">In campionato</div>
  <div class="ex-title"><h2>Prima di cominciare</h2></div>
  <div class="testo" style="margin-top:5mm">
    <p>Questi sono gli allenamenti veri della <b>Juniores provinciale che ha vinto il campionato senza perdere una partita</b>, trascritti dai quaderni dell'allenatore seduta per seduta e nell'ordine in cui sono stati svolti. Si parte dall'ultima seduta del precampionato (Allenamento 11) e si arriva alla quarta settimana di campionato.</p>
    <p>In campionato si lavora il <b>lunedì</b> e il <b>giovedì</b>. Dopo ogni giovedì trovi <b>la partita</b> del fine settimana con il risultato e le statistiche originali. Quattro partite, <b>quattro vittorie</b>, 11 gol fatti e 3 subiti.</p>
    <p>Ogni allenamento comincia con la <b>foto del foglio originale</b>. Poi la scheda della seduta (durata, programma e barra dei tempi), una pagina per ogni esercitazione e, dopo ogni esercitazione principale, una pagina di <b>indicazioni tecniche</b>.</p>
  </div>
  <h3 style="margin-top:5mm">Tre livelli di informazione</h3>
  <div class="box" style="font-size:10.2pt;line-height:1.5">
    <p style="margin-bottom:2mm"><span class="liv q">Dal quaderno</span>Esercitazioni, regole, punteggi, tempi e misure scritti sul foglio. Le pagine degli allenamenti li riportano così come sono.</p>
    <p style="margin-bottom:2mm"><span class="liv a">Precisato dall'autore</span>Chiarimenti dati dall'allenatore nel 2026, dove il foglio era incompleto o ambiguo.</p>
    <p><span class="liv c">Consigliato</span>Misure in metri dove il foglio non le riporta, obiettivi, punti di attenzione, errori da evitare e comportamenti da osservare. Sono indicazioni editoriali, non annotazioni storiche.</p>
  </div>
  <div class="nota-f"><b>Lavoro fisico.</b> Rapidità, corsa con variazioni di velocità, navette, flessioni e suicidi sono riportati come sono stati svolti con questa squadra, senza aggiungere carichi o recuperi. Non sono una prescrizione valida per ogni gruppo: vanno adattati all'età, al livello e alla condizione dei propri giocatori. I <b>suicidi</b> sono navette dalla linea dell'area piccola alla linea dell'area di rigore e ritorno: 11 m + 11 m, 22 m per navetta.</div>
  {FOOT}
</section>'''

intro2 = f'''<section class="page">
  <div class="kicker">In campionato</div>
  <div class="ex-title"><h2>Come leggere gli schemi</h2></div>
  <div class="legenda" style="margin-top:5mm">
    <div>{pallino("#2a5db0", testo="5")} Difensori e squadra di riferimento</div>
    <div>{pallino("#c8372d")} Attaccanti e avversari</div>
    <div>{pallino("#f2c230", "#1d2421")} Portiere</div>
    <div>{pallino("#ffffff", "#1d2421")} Jolly e sponde</div>
    <div>{freccia_oro} Movimento del giocatore</div>
    <div>{passaggio} Passaggio, lancio o cross</div>
  </div>
  <h3 style="margin-top:7mm">Tempi e misure</h3>
  <div class="testo">
    <p>Nei programmi delle sedute il tempo di ogni blocco è quello del quaderno. Nelle indicazioni tecniche trovi anche il <b>gioco effettivo</b>: quando il blocco dura più dei tempi di gioco (per esempio 35' per 2 tempi da 15'), la differenza è indicata come <b>non documentata</b>, senza inventare pause o recuperi.</p>
    <p>Le misure scritte dall'allenatore («metà campo», «3/4 di campo», «larga quanto l'area») restano come sono. Accanto trovi la misura in metri su un campo regolamentare da 105 × 68 m e, dove il foglio non dice nulla, una <b>misura consigliata</b>, sempre segnalata come tale.</p>
  </div>
  <div class="chiave" style="margin-top:7mm">
    <span class="kicker">Il libro</span>
    La stagione di questa squadra è raccontata nel libro <b>“Gli Imbattibili”</b>, su Amazon. Il libro racconta cosa è successo. Questi allenamenti mostrano come ci siamo arrivati.
  </div>
  {FOOT}
</section>'''


def campo_scheda(h, etichetta):
    m = re.search(rf'<div class="l">{etichetta}</div><div class="v">(.*?)</div>', h)
    return m.group(1) if m else ""


PARTITA = {13: "Euro Calcio Firenze 2-4 Spartaco Banti Barberino", 15: "Spartaco Banti Barberino 1-0 Fiesole",
           17: "Sagginale 1-5 Spartaco Banti Barberino", 19: "Spartaco Banti Barberino 1-0 Florence"}

blocchi = {i: pagine_allenamento(i) for i in N}
prima = 5  # copertina, prima di cominciare, schemi, indice: il primo allenamento parte da p. 5
inizio, p = {}, prima
for i in N:
    inizio[i] = p
    p += len(blocchi[i])
totale = p - 1

righe = []
for i in N:
    durata, focus = campo_scheda(html[i], "Durata"), campo_scheda(html[i], "Focus")
    giorno = " · ultima del precampionato" if i == 11 else (" · lunedì" if i % 2 == 0 else " · giovedì")
    partita = f'<div class="d" style="color:var(--oro)">+ la partita: {PARTITA[i]}</div>' if i in PARTITA else ""
    righe.append(f'<tr><td class="n">{i}</td><td><div class="t">Allenamento {i}{giorno}</div>'
                 f'<div class="d">{focus} · {durata}</div>{partita}</td><td class="p">p. {inizio[i]}</td></tr>')

indice = f'''<section class="page">
  <div class="kicker">In campionato</div>
  <div class="ex-title"><h2>Indice</h2></div>
  <table class="indice">{"".join(righe)}</table>
  {FOOT}
</section>'''

tutte = [copertina, intro, intro2, indice] + [s for i in N for s in blocchi[i]]
assert len(tutte) == totale
# numerazione continua: ogni "#" nel piè di pagina diventa il numero vero della pagina
numerate = [s.replace("<span>#</span>", f"<span>{n}</span>") for n, s in enumerate(tutte, 1)]

out = testa + "\n\n".join(numerate) + "\n\n</body>\n</html>\n"
(QUI / "campionato-allenamenti-11-19.html").write_text(out)
print("pagine:", totale, "· inizio allenamenti:", inizio)
