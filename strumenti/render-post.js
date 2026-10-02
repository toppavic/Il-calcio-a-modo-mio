// Salva ogni .slide di una pagina HTML come PNG (per i post social).
// Uso: NODE_PATH=$(npm root -g) node strumenti/render-post.js <file.html> <cartella> <prefisso>
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [html, cartella, prefisso] = process.argv.slice(2);
  fs.mkdirSync(cartella, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 2000 } });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const slide = await page.$$('.slide');
  for (let i = 0; i < slide.length; i++) {
    const post = Math.floor(i / 4) + 1, n = (i % 4) + 1;
    await slide[i].screenshot({ path: path.join(cartella, `${prefisso}-post${post}-${n}.png`) });
  }
  console.log(`${slide.length} immagini in ${cartella}`);
  await browser.close();
})();
