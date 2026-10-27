"""Genera le immagini dei post social (carosello) partendo dagli schemi degli allenamenti.

Crea post-4x5.html (Instagram e Facebook, 1080 × 1350) e post-9x16.html (TikTok, 1080 × 1920).
Le immagini PNG si ottengono con strumenti/render-post.js.
"""
import os
import pathlib
import re

QUI = pathlib.Path(__file__).parent
GI = QUI.parent.parent / "prodotti" / "gli-imbattibili"
a2 = (GI / "allenamento-02.html").read_text()
defs = re.search(r'<svg width="0" height="0".*?</svg>', a2, re.S).group(0)
FONT = "../../prodotti/gli-imbattibili/font"
MAT = "../../materiale"


def g(x, y, simbolo, n="", col="#fff"):
    t = (f'<text x="{x}" y="{y+4.5}" font-family="Oswald" font-size="13" font-weight="700" '
         f'text-anchor="middle" fill="{col}">{n}</text>') if n != "" else ""
    return f'<use href="#{simbolo}" x="{x}" y="{y}"/>{t}'


def freccia(d, oro=False, tratteggio=False):
    col, m = ("#f2c230", "freccia-oro") if oro else ("#fff", "freccia")
    da = ' stroke-dasharray="7 5"' if tratteggio else ""
    return f'<path d="{d}" stroke="{col}" stroke-width="2.5" fill="none"{da} marker-end="url(#{m})"/>'


def mezzo_campo(contenuto):
    return f'''<svg class="schema" viewBox="0 0 500 380">
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


# ---------- Schemi (identici a quelli dei PDF)
schema_cross = mezzo_campo(
    freccia("M236,350 L72,346", tratteggio=True)
    + freccia("M62,334 L58,104", tratteggio=True)
    + freccia("M40,250 L40,62", True)
    + freccia("M62,44 Q170,6 262,62", tratteggio=True)
    + g(40, 46, "pA", 2) + g(60, 346, "pA", 1) + g(440, 92, "pA") + g(450, 330, "pA")
    + g(250, 350, "pJ", "M", "#1d2421")
    + '<use href="#palla" x="56" y="54"/>'
    + g(140, 60, "pB", 2) + g(200, 74, "pB", 5) + g(262, 88, "pB", 6) + g(324, 102, "pB", 3)
    + g(172, 108, "pB", 4) + g(232, 122, "pB", 8))

# 4-2-3-1 (attacca verso destra: il 2 e il 7 sul lato destro, cioè in basso). Il 10 è quello che si gira.
blu = (g(80, 65, "pB", "3") + g(75, 125, "pB", "6") + g(75, 180, "pB", "5") + g(80, 240, "pB", "2")
       + g(160, 105, "pB", "8") + g(160, 205, "pB", "4")
       + g(275, 60, "pB", "11") + g(275, 245, "pB", "7") + g(395, 150, "pB", "9"))
rossi = (g(425, 70, "pA") + g(420, 125, "pA") + g(420, 185, "pA") + g(425, 235, "pA")
         + g(345, 95, "pA") + g(340, 200, "pA")
         + g(215, 60, "pA") + g(230, 120, "pA") + g(215, 245, "pA") + g(125, 150, "pA"))
schema_partita = f'''<svg class="schema" viewBox="0 0 500 300">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5">
      <rect x="30" y="20" width="440" height="260"/><line x1="250" y1="20" x2="250" y2="280"/>
      <rect x="14" y="128" width="16" height="44"/><rect x="470" y="128" width="16" height="44"/>
    </g>
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle">50 m</text>
    {g(30, 150, "pP", "P", "#1d2421")}{g(470, 150, "pP", "P", "#1d2421")}
    {rossi}{blu}
    {freccia("M87,178 L284,154", tratteggio=True)}
    <path d="M300,150 q14,-4 18,10 q2,10 -6,14" stroke="#f2c230" stroke-width="2.5" fill="none" marker-end="url(#freccia-oro)"/>
    {g(296, 150, "pB", "10")}{freccia("M316,149 L381,150", tratteggio=True)}
    <text x="300" y="128" font-family="Oswald" font-size="12" font-weight="700" fill="#fff" text-anchor="middle" letter-spacing="1">SI GIRA</text>
    <use href="#palla" x="88" y="190"/>
  </svg>'''

schema_gioco = f'''<svg class="schema" viewBox="60 0 380 340">
    <rect x="60" width="380" height="340" fill="url(#strisce)"/>
    <rect x="110" y="30" width="280" height="280" fill="none" stroke="#fff" stroke-width="2.5"/>
    <text x="250" y="332" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    <text x="415" y="175" font-family="Oswald" font-size="12" fill="#fff" text-anchor="middle">30 m</text>
    {freccia("M180,188 L240,117", tratteggio=True)}{freccia("M261,110 L361,214", tratteggio=True)}
    <use href="#palla" x="190" y="214"/>
    {g(250, 30, "pJ", 9, "#1d2421")}{g(250, 105, "pJ", 10, "#1d2421")}
    {g(140, 120, "pB", 11)}{g(185, 200, "pB", 4)}{g(370, 225, "pB", 2)}{g(235, 280, "pB", 5)}
    {g(360, 110, "pA", 7)}{g(235, 190, "pA", 8)}{g(140, 275, "pA", 3)}{g(305, 270, "pA", 6)}
  </svg>'''

def schema_ricerca_portiere():
    rossi = [(95, 70), (95, 150), (95, 230), (175, 110), (175, 190), (300, 150), (390, 100)]
    blu = [(405, 70), (405, 150), (405, 230), (325, 110), (325, 190), (200, 150), (110, 110)]
    gioc = "".join(g(x, y, "pA") for x, y in rossi) + "".join(g(x, y, "pB") for x, y in blu) + g(250, 230, "pJ", "J", "#1d2421")
    return f'''<svg class="schema" viewBox="0 0 500 300">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5"><rect x="40" y="20" width="420" height="260"/><line x1="250" y1="20" x2="250" y2="280"/></g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/><rect x="460" y="118" width="10" height="64" fill="#fff"/>
    {g(22, 150, "pP")}{g(478, 150, "pP")}
    {gioc}
    <use href="#palla" x="314" y="158"/>
    {freccia("M312,146 L462,150", tratteggio=True)}
  </svg>'''


def schema_specchio():
    dif_blu = [(95, 55), (95, 115), (95, 185), (95, 245)]
    att_rossi = [(165, 45), (165, 105), (165, 195), (165, 255), (215, 80), (215, 220)]
    dif_rossi = [(405, 55), (405, 115), (405, 185), (405, 245)]
    att_blu = [(335, 45), (335, 105), (335, 195), (335, 255), (285, 80), (285, 220)]
    gioc = ("".join(g(x, y, "pB") for x, y in dif_blu) + "".join(g(x, y, "pA") for x, y in att_rossi)
            + "".join(g(x, y, "pA") for x, y in dif_rossi) + "".join(g(x, y, "pB") for x, y in att_blu))
    return f'''<svg class="schema" viewBox="0 0 500 300">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5"><rect x="40" y="20" width="420" height="260"/><line x1="250" y1="20" x2="250" y2="280" stroke-dasharray="3 6"/></g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/><rect x="460" y="118" width="10" height="64" fill="#fff"/>
    {g(22, 150, "pP")}{g(478, 150, "pP")}
    {gioc}
    {freccia("M150,105 L112,113", True)}{freccia("M150,195 L112,187", True)}
    {freccia("M350,105 L388,113", True)}{freccia("M350,195 L388,187", True)}
    <use href="#palla" x="108" y="130"/>
    {freccia("M118,140 L322,112", tratteggio=True)}
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" letter-spacing="1">NESSUNO CAMBIA METÀ · LA PALLA SÌ</text>
  </svg>'''


def schema_tappa1():
    rossi = [(95, 50), (95, 110), (95, 190), (95, 250), (165, 105), (165, 195),
             (225, 50), (225, 150), (225, 250), (320, 150)]
    blu = [(405, 50), (405, 110), (405, 190), (405, 250), (335, 105), (335, 195),
           (275, 50), (275, 100), (275, 200), (180, 150)]
    gioc = "".join(g(x, y, "pA") for x, y in rossi) + "".join(g(x, y, "pB") for x, y in blu)
    return f'''<svg class="schema" viewBox="0 0 500 300">
    <rect width="500" height="300" fill="url(#strisce)"/>
    <g fill="none" stroke="#fff" stroke-width="2.5"><rect x="40" y="20" width="420" height="260"/><line x1="250" y1="20" x2="250" y2="280" stroke-dasharray="3 6"/></g>
    <rect x="30" y="118" width="10" height="64" fill="#fff"/><rect x="460" y="118" width="10" height="64" fill="#fff"/>
    {g(22, 150, "pP")}{g(478, 150, "pP")}
    {gioc}
    <use href="#palla" x="150" y="118"/>
    {freccia("M175,112 L225,128", tratteggio=True)}{freccia("M245,140 L305,150", tratteggio=True)}{freccia("M335,148 L458,150", tratteggio=True)}
    {freccia("M320,175 L355,165", True)}
    <text x="250" y="14" fill="#fff" font-family="Oswald" font-size="11" text-anchor="middle" letter-spacing="1">LA PALLA DEVE ARRIVARE AL PORTIERE</text>
  </svg>'''


# ---------- Contenuti dei post (regole e punti presi dai fogli dell'allenatore)
POST = [
    dict(
        n=1, foto="allenamento-04.jpg",
        gancio="Come difendevamo<span>sui cross</span>",
        schema=schema_cross,
        titolo2="La diagonale invertita",
        testo2="Il mister dà palla a <b>X1</b>, che la passa a <b>X2</b>. X2 arriva sul fondo e crossa. La linea si sistema per <b>respingere</b>.",
        titolo3="Chi va dove",
        punti=["Il <b>terzino lato palla</b> leggermente sotto la linea della palla",
               "<b>Centrali</b> e <b>terzino opposto</b> in leggera diagonale",
               "Il <b>centrocampista più vicino</b> a cerniera tra terzino e centrale",
               "<b>L'altro centrocampista</b> tra i due centrali"],
    ),
    dict(
        n=2, foto="allenamento-04-b.jpg",
        gancio="Preventiva<span>1</span>",
        schema=schema_partita,
        titolo2="Partita “lavoro preventivo”",
        testo2="10 contro 10 su 50 m. Chi riceve nella <b>metà campo offensiva</b> e riesce a girarsi e <b>servire un compagno</b> vale più di un gol. Chi difende deve stargli addosso <b>prima</b> che arrivi la palla.",
        titolo3="Le regole",
        punti=["<b>2 tempi da 15'</b>",
               "Massimo <b>3 tocchi</b>",
               "<b>Gol = 1 punto</b>",
               "Chi riceve nella <b>metà campo offensiva</b>, ha il tempo di girarsi e fa un passaggio <b>verticale o diagonale</b> a un compagno:&nbsp;<b>2&nbsp;punti</b>"],
    ),
    dict(
        n=3, foto="allenamento-03.jpg", cop_schema=True,
        gancio="8 passaggi<span>= 1 punto</span>",
        schema=schema_gioco,
        titolo2="Gioco di posizione",
        testo2="<b>4 contro 4 + 2 jolly</b> (il 9 e il 10) in un quadrato di <b>30 × 30 m</b>. <b>8 passaggi</b> consecutivi = <b>1 punto</b>.",
        titolo3="Per renderlo difficile",
        punti=["Si gioca a <b>2 tocchi</b>",
               "I jolly hanno <b>1 solo tocco</b>",
               "Con meno tocchi bisogna <b>smarcarsi prima</b> e più in fretta"],
    ),
    dict(
        n=4, foto="allenamento-01.jpg", ponte=True,
        gancio="Ci chiesero<span>il quinto posto</span>",
        kicker2="Allenamento 1",
        titolo2="La prima seduta",
        lista2=["<b>10'</b> Riscaldamento",
                "<b>30'</b> Partita “ricerca del portiere”",
                "<b>20'</b> Circuito atletico",
                "<b>2 × 15-20'</b> Lavoro a gruppi: linea difensiva e gioco di posizione",
                "<b>5'</b> Defaticamento"],
        titolo3="Ricerca del portiere",
        punti=["Due squadre da 10 e <b>un portiere per lato</b> che fa da bersaglio",
               "<b>1° tempo</b>: massimo 3 tocchi, portiere trovato = 1 punto",
               "<b>2° tempo</b>: massimo 2 tocchi, lancio dalla metà difensiva = 2 punti"],
        fine_sub="Vuoi l'allenamento completo con gli schemi? Scrivi <b>PRECAMPIONATO</b> nei commenti. La storia di quella stagione è nel libro.",
        azioni=["Scrivi PRECAMPIONATO", "Il libro è nel link in bio"],
    ),
    dict(
        n=5, foto="allenamento-16.jpg", cartella="campionato", tema="chiaro",
        gancio="Recupero alto<span>= 2 punti</span>",
        schema=schema_ricerca_portiere(),
        titolo2="Ricerca del portiere",
        testo2="<b>7 contro 7 + jolly</b> in due metà campo, con un <b>portiere bersaglio</b> per lato. Si può fare dal <b>7 contro 7</b> all'<b>11 contro 11</b> cambiando le dimensioni del campo.",
        obiettivo="<span>Obiettivo primario</span>Pressione di squadra in metà offensiva<span class='sec'>Obiettivo secondario</span><i>La linea di difesa, persa palla, toglie le filtranti</i>",
        titolo3="Le regole",
        punti=["<b>2 tempi da 15'</b>",
               "Massimo <b>3 tocchi</b>, niente lancio",
               "Recuperi palla nella <b>metà offensiva</b> e fai gol: <b>2 punti</b>",
               "Nel 2° tempo <b>solo gioco verticale</b>",
               "Il portiere riceve la palla <b>solo dentro la porta</b>: si migliora anche la qualità del passaggio"],
        fine_sub="La Juniores che ha vinto il campionato <b>senza perdere una partita</b>. Gli allenamenti in campionato, scritti a mano dal mister e messi in pagina.",
    ),
    dict(
        n=6, senza_foto=True, cop_schema=True, tema="verde",
        gancio="Preventiva<span>2</span>",
        schema=schema_specchio(),
        titolo2="Partita a specchio",
        testo2="<b>10 contro 10</b> più i portieri. Mezzo campo diviso in due metà: in ciascuna giocano <b>6 attaccanti</b> di una squadra contro i <b>4 difensori</b> dell'altra. La palla circola liberamente tra le metà mentre i giocatori restano nella propria: la difesa lavora sempre in <b>inferiorità numerica</b>.",
        obiettivo="<span>Obiettivo primario</span>Pressione sui 4 difensori<i>L'uscita della palla deve essere forzata, mai pulita</i><span class='sec'>Obiettivo secondario</span><i>Le marcature preventive</i>",
        titolo3="Le regole",
        punti=["<b>2 tempi da 15'</b>",
               "Attaccanti a <b>3 tocchi</b>, difensori <b>liberi</b>",
               "<b>Gol = 1 punto</b>",
               "Nessun giocatore può passare nell'altra metà: <b>circola solo la palla</b>",
               "Campo: <b>mezzo campo</b> diviso in due, di almeno <b>50 m</b>",
               "Da <b>8 contro 8</b> a <b>11 contro 11</b>. Con numeri dispari entra un <b>jolly</b> libero di muoversi"],
        fine_sub="Secondo gradino del percorso sulla <b>marcatura preventiva</b>. La Juniores che ha vinto il campionato <b>senza perdere una partita</b>.",
    ),
    dict(
        n=7, senza_foto=True, tema="oro",
        gancio="Se corri solo tu<span style=\"margin-top:16px\">hai già perso</span>", h1style="font-size:118px;line-height:1.05",
        sub="Si corre insieme <b>o si scappa</b>.",
        kick="Dai quaderni del mister", marchio="DAI QUADERNI DEL MISTER", fine_h1="Dai quaderni<span>del mister</span>",
        kicker2="La ricerca del portiere",
        titolo2="Vuoi una squadra che&hellip;",
        lista2=["metta <b>pressione</b> prima che l'avversario abbia il tempo di lanciare?",
                "sappia <b>accorciare</b> senza regalare spazio alle proprie spalle?",
                "riconosca il momento in cui deve <b>scappare</b> e proteggere la profondità?",
                "sappia <b>verticalizzare</b> con precisione, invece di buttare avanti il pallone?"],
        kicker3="La ricerca del portiere",
        titolo3="E se per allenare tutto questo non dovessi segnare un gol?",
        punti=["Il bersaglio è il <b>portiere avversario</b>",
               "Chi attacca deve <b>trovarlo con precisione</b>",
               "Chi difende deve <b>impedire che venga trovato</b>",
               "Due squadre. Due problemi. <b>Decisioni continue</b>"],
        titolo_ob="Una progressione",
        obiettivo="<span>7 tappe</span>Non servono 7 esercizi diversi<i>Serve una progressione che abbia un senso</i>",
        fine_sub="Difficoltà crescente. Regole che cambiano per allenare decisioni sempre più complesse. La progressione completa <b>ricerca del portiere</b> arriva presto su Etsy. Link in bio.",
        fine_sub_tt="Difficoltà crescente. Regole che cambiano per allenare decisioni sempre più complesse. La progressione completa <b>ricerca del portiere</b> arriva presto su Etsy. Cercaci: <b>ilcalcioamodomio</b>.",
        azioni=["Salva il post", "Seguici per l'uscita"],
    ),
    dict(
        n=8, senza_foto=True, cop_schema=True, tema="oro",
        gancio="Trova<span>il portiere</span>",
        sub="Il gol non esiste · <b>Tappa 1 di 7</b>",
        schema=schema_tappa1(),
        titolo2="Ricerca del portiere",
        testo2="<b>10 contro 10</b> in due metà campo, con un <b>portiere bersaglio</b> per lato corto. Non ci sono porte: ogni volta che la palla arriva al portiere avversario la squadra fa <b>1 punto</b>.",
        obiettivo="<span>Obiettivo primario</span>Circolazione di palla funzionale<i>Ogni passaggio avvicina la palla al portiere</i><span class='sec'>Obiettivo secondario</span><i>Smarcarsi e testa alta</i>",
        titolo3="Le regole",
        punti=["<b>15 minuti</b>",
               "Massimo <b>3 tocchi</b>",
               "Portiere trovato = <b>1 punto</b>",
               "Campo: <b>50 m</b> di lunghezza per tutta la larghezza, diviso in <b>due metà</b>",
               "Chi difende resta <b>corto</b> e attento alle spalle"],
        fine_sub="Prima tappa di un percorso in <b>7 tappe</b> per imparare a pressare insieme. Salva il post: la prossima tappa cambia le regole.",
        azioni=["Salva il post", "Seguici per la tappa 2"],
    ),
    dict(
        n=9, senza_foto=True, tema="chiaro",
        gancio="Pressare è<span>individuale</span>", h1style="font-size:128px",
        sub="Farlo insieme è un comportamento <b>che si allena</b>.",
        kick="Dai quaderni del mister", marchio="DAI QUADERNI DEL MISTER", fine_h1="Dai quaderni<span>del mister</span>",
        kicker2="La pressione organizzata",
        titolo2="Si può insegnare?",
        lista2=["Non basta insegnare a un giocatore <b>quando uscire</b> sull'avversario.",
                "Bisogna insegnare agli altri <b>cosa fare mentre lui ci va</b>.",
                "Come si insegna a una squadra a <b>muoversi insieme</b>?"],
        kicker3="La ricerca del portiere",
        titolo3="Un bersaglio per muoversi insieme",
        punti=["Il <b>portiere avversario</b> diventa il bersaglio",
               "Attorno a lui si <b>costruisce</b>, si <b>organizza</b> e si <b>codifica</b> la pressione"],
        fine_sub="Percorso 1, <b>La ricerca del portiere</b>: 7 tappe per allenare la pressione di squadra. Link in bio.",
        fine_sub_tt="Percorso 1, <b>La ricerca del portiere</b>: 7 tappe per allenare la pressione di squadra. Cercaci: <b>ilcalcioamodomio</b>.",
        azioni=["Salva il post", "Seguici"],
    ),
]

FIRMA = "La Juniores che ha vinto il campionato <b>senza perdere una partita</b>"


def slides(p, tot=None, h=1350):
    tot = tot or (5 if p.get("obiettivo") else 4)
    num = lambda i: f'<div class="num">{i}/{tot}</div>'
    marchio = '<div class="marchio"><b>' + (p.get("marchio") or "GLI IMBATTIBILI") + '</b><span>Il calcio a modo mio</span></div>'
    punti = "".join(f"<li>{x}</li>" for x in p["punti"])
    if p.get("lista2"):
        lista2 = "".join(f"<li>{x}</li>" for x in p["lista2"])
        slide2 = f'''<section class="slide int">
  {num(2)}
  <div class="kicker">{p["kicker2"]}</div>
  <h2>{p["titolo2"]}</h2>
  <ul class="punti">{lista2}</ul>
  {marchio}
</section>'''
    else:
        slide2 = f'''<section class="slide int">
  {num(2)}
  <div class="kicker">Esercitazione</div>
  <h2>{p["titolo2"]}</h2>
  <div class="riq">{p["schema"]}</div>
  <p class="desc">{p["testo2"]}</p>
  {marchio}
</section>'''
    return f'''
<section class="slide cop{' cs' if p.get('cop_schema') else ''} t-{p.get('tema') or os.environ.get('TEMA') or 'scuro'}">
  {'' if p.get("senza_foto") else '<img class="bgimg" src="' + MAT + '/' + p.get("cartella", "precampionato") + '/' + p["foto"] + '">'}
  <div class="veil"></div>
  <img class="logo" src="{MAT}/brand/logo-cerchio.png">
  {('<div class="copschema"' + (' style="width:' + str(567 if h > 1500 else 433) + 'px"' if p.get("senza_foto") else '') + '>' + p["schema"].replace('class="schema"', 'preserveAspectRatio="xMidYMid ' + ('meet' if p.get("senza_foto") else 'slice') + '"') + '</div>') if p.get("cop_schema") else ''}
  <div class="txt">
    <div class="kick">{p.get("kick") or "Gli Imbattibili · dai quaderni del mister"}</div>
    <h1 style="{p.get("h1style") or ""}">{p["gancio"]}</h1>
    <p class="sub">{p.get("sub") or FIRMA}</p>
    <div class="scorri">Scorri →</div>
  </div>
</section>
{slide2}
<section class="slide int">
  {num(3)}
  <div class="kicker">{p.get("kicker3") or p["titolo2"]}</div>
  <h2>{p["titolo3"]}</h2>
  <ul class="punti">{punti}</ul>
  {marchio}
</section>
{('<section class="slide int">' + num(4) + '<div class="kicker">' + (p.get("kicker3") or p["titolo2"]) + '</div><h2>' + p.get("titolo_ob", "Gli obiettivi") + '</h2><div class="obiettivo">' + p["obiettivo"] + '</div>' + marchio + '</section>') if p.get("obiettivo") else ''}
<section class="slide fine">
  <img class="logo2" src="{MAT}/brand/logo-cerchio.png">
  <h1>{p.get("fine_h1") or "Gli<span>Imbattibili</span>"}</h1>
  <p class="sub">{(p.get("fine_sub_tt") if h > 1500 and p.get("fine_sub_tt") else p.get("fine_sub")) or (FIRMA + ". Gli allenamenti del precampionato, scritti a mano dal mister e messi in pagina.")}</p>
  <div class="azioni">{"".join("<div>" + a + "</div>" for a in (p.get("azioni") or ["Salva il post", "Seguici per il prossimo"]))}</div>
</section>'''


def pagina(w, h):
    alto = h > 1500
    css = f'''
@font-face {{ font-family: Oswald; src: url({FONT}/oswald.woff2) format("woff2"); font-weight: 200 700; }}
@font-face {{ font-family: Inter; src: url({FONT}/inter.woff2) format("woff2"); font-weight: 100 900; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #888; font-family: Inter, sans-serif; }}
.slide {{ width: {w}px; height: {h}px; position: relative; overflow: hidden; margin: 0 0 20px; }}
h1, h2 {{ font-family: Oswald, sans-serif; font-weight: 700; text-transform: uppercase; }}
.cop, .fine {{ background: #0c120f; color: #fff; }}
.cop .bgimg {{ position: absolute; inset: -40px; width: calc(100% + 80px); height: calc(100% + 80px); object-fit: cover; transform: rotate(-4deg) scale(1.08); filter: grayscale(1) contrast(1.1); opacity: .55; }}
.cop .veil {{ position: absolute; inset: 0; background: linear-gradient(180deg, rgba(12,18,15,.97) 0%, rgba(12,18,15,.9) 36%, rgba(12,18,15,.5) 52%, rgba(12,18,15,.85) 66%, rgba(12,18,15,.98) 80%); }}
.cop .logo {{ position: absolute; top: {170 if alto else 40}px; left: 50%; transform: translateX(-50%); width: {440 if alto else 520}px; -webkit-mask-image: linear-gradient(180deg, #000 80%, transparent 100%); }}
.copschema {{ position: absolute; left: 50%; transform: translateX(-50%); top: {650 if alto else 480}px; width: {700 if alto else 560}px; height: {340 if alto else 260}px; border-radius: 18px; overflow: hidden; border: 3px solid rgba(132,185,74,.6); }}
.cop.cs .txt {{ {'top: 1040px' if alto else ''} }}
.copschema svg {{ width: 100%; height: 100%; display: block; }}
.cop .txt {{ position: absolute; left: 80px; right: 80px; {'top: 860px' if alto else 'bottom: 80px'}; }}
.kick {{ font-family: Oswald, sans-serif; font-weight: 500; letter-spacing: .22em; text-transform: uppercase; font-size: 28px; color: #84b94a; }}
.cop h1, .fine h1 {{ font-size: {150 if alto else 130}px; line-height: .92; margin: 20px 0 28px; }}
.cop h1 span, .fine h1 span {{ color: #84b94a; display: block; }}
.sub {{ font-size: 36px; line-height: 1.4; color: #dfe6e1; }}
.sub b {{ color: #fff; }}
.scorri {{ margin-top: 40px; font-family: Oswald, sans-serif; text-transform: uppercase; letter-spacing: .15em; font-size: 30px; color: #84b94a; }}
.cop.t-verde {{ background: #0f3d2e; }}
.cop.t-verde .veil {{ background: linear-gradient(180deg, rgba(15,61,46,.97) 0%, rgba(15,61,46,.9) 36%, rgba(15,61,46,.5) 52%, rgba(15,61,46,.88) 66%, rgba(15,61,46,.98) 80%); }}
.cop.t-verde .kick, .cop.t-verde h1 span, .cop.t-verde .scorri {{ color: #d4a017; }}
.cop.t-oro .kick, .cop.t-oro h1 span, .cop.t-oro .scorri {{ color: #d4a017; }}
.cop.t-chiaro {{ background: #f3efe4; color: #0f3d2e; }}
.cop.t-chiaro .bgimg {{ opacity: .22; }}
.cop.t-chiaro .veil {{ background: linear-gradient(180deg, rgba(243,239,228,.97) 0%, rgba(243,239,228,.85) 36%, rgba(243,239,228,.4) 52%, rgba(243,239,228,.8) 66%, rgba(243,239,228,.97) 80%); }}
.cop.t-chiaro h1 {{ color: #0f3d2e; }}
.cop.t-chiaro .kick, .cop.t-chiaro h1 span, .cop.t-chiaro .scorri {{ color: #b8860b; }}
.cop.t-chiaro .sub {{ color: #26352d; }}
.cop.t-chiaro .sub b {{ color: #0f3d2e; }}
.int {{ background: #fff; padding: {'0 80px 260px' if alto else '90px 80px 0'}; color: #1d2421; {'display: flex; flex-direction: column; justify-content: center;' if alto else ''} }}
.int .num {{ position: absolute; top: {90 if alto else 40}px; right: 60px; font-family: Oswald, sans-serif; font-size: 28px; color: #9aa59f; }}
.kicker {{ font-family: Oswald, sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: .2em; font-size: 28px; color: #d4a017; }}
.int h2 {{ font-size: 78px; line-height: 1.02; color: #0f3d2e; margin: 10px 0 40px; }}
.riq {{ display: flex; justify-content: center; }}
.riq .schema {{ width: 100%; max-height: {900 if alto else 700}px; display: block; border-radius: 16px; }}
.desc {{ font-size: 36px; line-height: 1.45; margin-top: 40px; }}
.obiettivo {{ margin-top: 50px; padding: 50px 44px; border-radius: 18px; background: #0f3d2e; color: #fff; font-family: Oswald, sans-serif; text-transform: uppercase; font-size: 76px; line-height: 1.1; font-weight: 600; }}
.obiettivo i {{ display: block; font-style: normal; font-size: 64px; }}
.obiettivo span.sec {{ margin-top: 56px; }}
.obiettivo span {{ display: block; color: #d4a017; font-size: 32px; letter-spacing: .18em; font-weight: 500; margin-bottom: 14px; }}
.desc b, .punti b {{ color: #0f3d2e; }}
.punti {{ list-style: none; margin-top: 20px; }}
.punti li {{ font-size: 42px; line-height: 1.35; padding: 34px 0 34px 70px; position: relative; border-bottom: 2px solid #e3e8e5; }}
.punti li::before {{ content: ""; position: absolute; left: 0; top: 50px; width: 30px; height: 30px; background: #d4a017; border-radius: 50%; }}
.marchio {{ position: absolute; left: 80px; right: 80px; bottom: {150 if alto else 50}px; display: flex; justify-content: space-between; align-items: center; border-top: 3px solid #0f3d2e; padding-top: 22px; font-size: 26px; color: #5d6b65; }}
.marchio b {{ font-family: Oswald, sans-serif; color: #0f3d2e; letter-spacing: .12em; font-weight: 600; font-size: 30px; }}
.fine {{ display: flex; flex-direction: column; justify-content: center; padding: 0 80px; }}
.fine .logo2 {{ width: 340px; margin: 0 0 30px -20px; -webkit-mask-image: linear-gradient(180deg, #000 75%, transparent 100%); }}
.azioni {{ display: flex; gap: 24px; margin-top: 60px; }}
.azioni div {{ flex: 1; text-align: center; font-family: Oswald, sans-serif; text-transform: uppercase; letter-spacing: .08em; font-size: 32px; padding: 26px 10px; border-radius: 14px; background: #84b94a; color: #0c120f; }}
.azioni div + div {{ background: transparent; color: #fff; border: 2px solid #84b94a; }}
'''
    corpo = "".join(slides(p, h=h) for p in POST if not os.environ.get("SOLO") or str(p["n"]) in os.environ["SOLO"].split(","))
    return f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Post social</title><style>{css}</style></head><body>{defs}{corpo}</body></html>'


SUF = ("-solo" + os.environ["SOLO"].replace(",", "")) if os.environ.get("SOLO") else ""
(QUI / f"post{SUF}-4x5.html").write_text(pagina(1080, 1350))
(QUI / f"post{SUF}-9x16.html").write_text(pagina(1080, 1920))
print("ok")
