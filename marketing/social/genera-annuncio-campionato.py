"""Carosello di annuncio del pacchetto "In campionato" (15/10/2026): 4 pagine, 4:5 e 9:16."""
import pathlib
QUI = pathlib.Path(__file__).parent
FONT = "../../prodotti/gli-imbattibili/font"
LOGO = "../../materiale/brand/logo-cerchio.png"
P = "../etsy/pagine-campionato/"

LISTA = [("11", "Rapidità e sponde"), ("12", "Arrivare in meta"), ("13", "Gioco verticale e palle inattive"),
         ("14", "Difesa in superiorità"), ("15", "Pressione e preventive"), ("16", "Ricerca del portiere"),
         ("17", "Pressione e rapidità"), ("18", "Gioco sulla punta"), ("19", "Attacco alla meta")]


def pagina(w, h):
    alto = h > 1500
    lista = "".join(f"<div><b>{n}</b><span>{t}</span></div>" for n, t in LISTA)
    css = f'''
@font-face {{ font-family: Oswald; src: url({FONT}/oswald.woff2) format("woff2"); font-weight: 200 700; }}
@font-face {{ font-family: Inter; src: url({FONT}/inter.woff2) format("woff2"); font-weight: 100 900; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: #888; font-family: Inter, sans-serif; }}
.slide {{ width: {w}px; height: {h}px; position: relative; overflow: hidden; margin: 0 0 20px; background: #0f3d2e; color: #fff; padding: 0 80px; }}
.kick {{ font-family: Oswald; letter-spacing: .2em; text-transform: uppercase; color: #d4a017; font-size: 30px; font-weight: 500; }}
h1, h2 {{ font-family: Oswald; text-transform: uppercase; font-weight: 700; line-height: .95; }}
h1 {{ font-size: {150 if alto else 140}px; }} h1 span {{ color: #d4a017; display: block; }}
h2 {{ font-size: 86px; line-height: 1; margin-top: 18px; }}
.sub {{ font-size: 38px; line-height: 1.4; color: #dfe6e1; margin-top: 34px; }} .sub b {{ color: #fff; }}
.logo {{ position: absolute; top: {150 if alto else 40}px; left: 50%; transform: translateX(-50%); width: {440 if alto else 400}px; -webkit-mask-image: linear-gradient(180deg, #000 80%, transparent 100%); }}
.txt {{ position: absolute; left: 80px; right: 80px; top: {700 if alto else 470}px; }}
.scorri {{ margin-top: 40px; font-family: Oswald; text-transform: uppercase; letter-spacing: .15em; font-size: 30px; color: #d4a017; }}
.int {{ padding-top: {200 if alto else 90}px; }}
.lista {{ margin-top: 24px; }}
.lista div {{ display: flex; align-items: baseline; gap: 26px; border-bottom: 2px solid rgba(255,255,255,.16); padding: {8 if not alto else 14}px 0; }}
.lista b {{ font-family: Oswald; font-size: 46px; color: #d4a017; width: 80px; flex: none; }}
.lista span {{ font-family: Oswald; text-transform: uppercase; font-size: 34px; }}
.bil {{ margin-top: 22px; background: #d4a017; color: #0f3d2e; border-radius: 14px; padding: 20px 28px; font-family: Oswald; text-transform: uppercase; font-size: 32px; font-weight: 700; line-height: 1.15; }}
.pag {{ position: absolute; border-radius: 8px; box-shadow: 0 24px 60px rgba(0,0,0,.55); background: #fff; }}
.num {{ position: absolute; top: 40px; right: 50px; font-family: Oswald; font-size: 26px; color: rgba(255,255,255,.5); }}
.marchio {{ position: absolute; left: 80px; right: 80px; bottom: {150 if alto else 50}px; border-top: 3px solid #d4a017; padding-top: 20px; display: flex; justify-content: space-between; font-size: 26px; color: #c9d4cd; }}
.marchio b {{ font-family: Oswald; letter-spacing: .12em; color: #fff; font-size: 30px; }}
.fine {{ display: flex; flex-direction: column; justify-content: center; }}
.fine .logo2 {{ width: 340px; margin: 0 0 30px -20px; -webkit-mask-image: linear-gradient(180deg, #000 75%, transparent 100%); }}
.azioni {{ display: flex; gap: 24px; margin-top: 60px; }}
.azioni div {{ flex: 1; text-align: center; font-family: Oswald; text-transform: uppercase; letter-spacing: .08em; font-size: 32px; padding: 26px 10px; border-radius: 14px; background: #d4a017; color: #0f3d2e; }}
.azioni div + div {{ background: transparent; color: #fff; border: 2px solid #d4a017; }}
'''
    marchio = '<div class="marchio"><b>GLI IMBATTIBILI</b><span>Il calcio a modo mio</span></div>'
    top = 560 if alto else 360
    s1 = f'''<section class="slide"><img class="logo" src="{LOGO}">
<div class="txt"><div class="kick">Gli Imbattibili · In campionato</div>
<h1 style="margin-top:22px">Le prime<span>4 settimane</span></h1>
<p class="sub">Dopo la preparazione: <b>9 allenamenti</b> della Juniores che ha vinto il campionato <b>senza perdere una partita</b>.</p>
<div class="scorri">Scorri →</div></div></section>'''
    s2 = f'''<section class="slide int"><div class="num">2/4</div><div class="kick">Lunedì e giovedì</div><h2>9 allenamenti</h2>
<div class="lista">{lista}</div>
<div class="bil">+ 4 partite: 4 vittorie, 11 gol fatti e 3 subiti</div>{marchio}</section>'''
    s3 = f'''<section class="slide int"><div class="num">3/4</div><div class="kick">Dentro il PDF</div><h2>Ogni seduta e ogni partita</h2>
<img class="pag" src="{P}p-13-13.png" style="left:60px;top:{top+60}px;width:480px;transform:rotate(-5deg)">
<img class="pag" src="{P}p-17-17.png" style="right:60px;top:{top+60}px;width:480px;transform:rotate(5deg)">
<img class="pag" src="{P}p-30-30.png" style="left:290px;top:{top}px;width:500px">
{marchio}</section>'''
    s4 = f'''<section class="slide fine"><img class="logo2" src="{LOGO}">
<h1>Gli<span>Imbattibili</span></h1>
<p class="sub"><b>In campionato</b>: le prime 4 settimane. PDF · 46 pagine · schemi, regole e partite.</p>
<div class="azioni"><div>Link in bio</div><div>Salva il post</div></div></section>'''
    return f'<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Annuncio In campionato</title><style>{css}</style></head><body>{s1}{s2}{s3}{s4}</body></html>'


(QUI / "annuncio-campionato-4x5.html").write_text(pagina(1080, 1350))
(QUI / "annuncio-campionato-9x16.html").write_text(pagina(1080, 1920))
print("ok")
