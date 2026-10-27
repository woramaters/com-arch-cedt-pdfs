# com-arch-cedt-pdfs

ไฟล์เตรียมสอบวิชา Computer Architecture (+ Digital Logic)

| ไฟล์ | เนื้อหา |
|---|---|
| `Exam-Notes.pdf` | สรุปละเอียดทุกบท อธิบายทุกคำศัพท์ (ย่อมาจาก / คืออะไร / ทำหน้าที่ / ทำงานอย่างไร / สัมพันธ์กับอะไร) พร้อม Formula Sheet, กับดัก และ Glossary A–Z |
| `Mock-Exam.pdf` | ข้อสอบเสมือนจริง 2 ชุด (ชุดที่ 1 ตามเกณฑ์จริง 60 คะแนน, ชุดที่ 2 ข้อเขียนยาว 100 คะแนน) พร้อมเฉลยละเอียดท้ายเล่ม |
| `com_arch_pdf_combined.pdf` | สไลด์ต้นฉบับ |

## แก้ไขและ build ใหม่

ต้นฉบับเป็น markdown อยู่ใน `src/notes/` และ `src/exam/` (ไฟล์ถูกรวมตามลำดับชื่อ) ใช้ pandoc แปลงเป็น HTML แล้ว Chromium (Playwright) พิมพ์เป็น PDF:

```sh
node src/build.mjs
```

ต้องมี `pandoc` และ `playwright` (Chromium) ส่วนฟอนต์ Sarabun และ JetBrains Mono (OFL) อยู่ใน `src/fonts/`
