// Registra una pagina animata (funzione draw(t)) fotogramma per fotogramma e crea un MP4 verticale.
// Uso: NODE_PATH=$(npm root -g) node strumenti/render-reel.js <file.html> <uscita.mp4> <secondi> [fps]
const path = require('path');
const fs = require('fs');
const os = require('os');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

(async () => {
  const [html, out, durata, fpsArg] = process.argv.slice(2);
  const fps = Number(fpsArg || 30);
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'reel-'));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const n = Math.round(Number(durata) * fps);
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => draw(t), i / fps);
    await page.screenshot({ path: path.join(tmp, `f${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
  }
  await browser.close();
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(tmp, 'f%05d.jpg'),
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-movflags', '+faststart', out]);
  fs.rmSync(tmp, { recursive: true });
  console.log(`${out} · ${n} fotogrammi`);
})();
