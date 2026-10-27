// Build the study PDFs: markdown parts -> pandoc HTML -> Chromium PDF.
// Usage: node src/build.mjs   (run from the repository root)
import { execFileSync } from 'node:child_process';
import { readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { createRequire } from 'node:module';

// Playwright is installed globally; ESM import cannot see it, require() can.
const { chromium } = createRequire(import.meta.url)('playwright');

const SRC = resolve('src');
const PANDOC_FROM =
  'markdown-tex_math_dollars-subscript-superscript-citations-smart-implicit_figures-fancy_lists+ascii_identifiers+lists_without_preceding_blankline';

const docs = [
  { dir: 'notes', out: 'Exam-Notes.pdf', title: 'Computer Architecture + Digital Logic: Exam Notes', toc: true, cover: 'cover-notes.html' },
  { dir: 'exam', out: 'Mock-Exam.pdf', title: 'Mock Exam + Solutions', toc: false, cover: 'cover-exam.html' },
];

const browser = await chromium.launch();
for (const doc of docs) {
  const dir = join(SRC, doc.dir);
  const parts = readdirSync(dir).filter((f) => f.endsWith('.md')).sort().map((f) => join(dir, f));
  const html = join(SRC, `${doc.dir}.html`);
  const args = ['-f', PANDOC_FROM, '-t', 'html5', '-s', '--template', join(SRC, 'template.html'),
    '--metadata', `title=${doc.title}`, '-o', html];
  if (doc.toc) args.push('--toc', '--toc-depth=2');
  if (doc.cover) args.push('--include-before-body', join(SRC, doc.cover));
  execFileSync('pandoc', [...args, ...parts], { stdio: 'inherit' });

  const page = await browser.newPage();
  await page.goto('file://' + html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: resolve(doc.out),
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate:
      `<div style="width:100%;font-size:8px;color:#8a96a6;padding:0 15mm;display:flex;justify-content:space-between;font-family:sans-serif">` +
      `<span>${doc.title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    margin: { top: '14mm', bottom: '16mm', left: '15mm', right: '15mm' },
  });
  await page.close();
  console.log('built', doc.out);
}
await browser.close();
