# Part 0: Digital Logic (15 คะแนน)

> ไฟล์ PDF ที่ได้รับไม่มีสไลด์ Digital Logic ส่วนนี้จึงอิงเนื้อหามาตรฐานของวิชา Digital Computer Logic (สไลด์ Com Arch อ้างถึงหนังสือ *Contemporary Logic Design* ของ Randy Katz) และเน้นหัวข้อที่ Com Arch นำไปใช้ต่อ

## 0.1 ระบบเลข (Number Systems)

::: term
[Bit]{.abbr} [Binary digit]{.full} [เลขฐานสองหนึ่งหลัก]{.th}

- **คืออะไร:** หน่วยข้อมูลที่เล็กที่สุด มีค่าได้แค่ 0 หรือ 1
- **ทำงานอย่างไร:** ในวงจรแทนด้วยแรงดันต่ำ (0) หรือสูง (1)
- **สัมพันธ์กับ:** 8 bits = 1 **byte** · 4 bits = 1 **nibble** (= เลขฐาน 16 หนึ่งหลัก) · n bits แทนค่าได้ **2ⁿ แบบ**
:::

::: term
[Radix / Base]{.abbr} [ฐานของระบบเลข]{.th}

- **คืออะไร:** จำนวนสัญลักษณ์ที่ใช้ในระบบเลข เช่น ฐาน 2 (binary), 8 (octal), 10 (decimal), 16 (hexadecimal)
- **ทำงานอย่างไร:** หลักที่ i มีค่าประจำหลักเป็น base^i เช่น (1011.01)₂ = 1·2³ + 0·2² + 1·2¹ + 1·2⁰ + 0·2⁻¹ + 1·2⁻² = **11.25**
- **สัมพันธ์กับ:** **Hex** ใช้แทน binary แบบสั้น (1 hex = 4 bits) ซึ่ง address และ opcode ในวิชา Com Arch เขียนเป็น hex เสมอ
:::

### วิธีแปลงฐาน

| จาก → ไป | วิธี | ตัวอย่าง |
|---|---|---|
| ฐานใดก็ได้ → ฐาน 10 | คูณแต่ละหลักด้วยค่าประจำหลักแล้วรวม | (1011.01)₂ = 11.25 |
| ฐาน 10 → ฐาน 2 (จำนวนเต็ม) | หาร 2 ซ้ำ ๆ แล้ว**อ่านเศษจากล่างขึ้นบน** | 13 → 1101 |
| ฐาน 10 → ฐาน 2 (ทศนิยม) | คูณ 2 ซ้ำ ๆ แล้ว**อ่านหลักหน้าจุดจากบนลงล่าง** | 0.375 → .011 |
| ฐาน 2 ↔ ฐาน 16 | จัดกลุ่มทีละ **4 bits** เริ่มจากจุด | 1111 0111 = 0xF7 |
| ฐาน 2 ↔ ฐาน 8 | จัดกลุ่มทีละ **3 bits** เริ่มจากจุด | 0x3F7 = 001 111 110 111 = **1767₈** |

| Dec | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |

ค่ายกกำลังของ 2 ที่ควรจำ: 2¹⁰ = 1024 (K), 2²⁰ ≈ 1M, 2³⁰ ≈ 1G, 2³² = 4G

## 0.2 การแทนเลขมีเครื่องหมาย (Signed Numbers)

::: term
[MSB / LSB]{.abbr} [Most / Least Significant Bit]{.full} [บิตที่มีค่าประจำหลักมากที่สุด / น้อยที่สุด]{.th}

- **คืออะไร:** MSB คือบิตซ้ายสุด ส่วน LSB คือบิตขวาสุด
- **ทำหน้าที่:** ในเลขมีเครื่องหมาย MSB เป็น **sign bit** (0 = บวก, 1 = ลบ)
- **สัมพันธ์กับ:** **Endian** (Ch3) คือการเลือกว่าจะเก็บ byte ที่มี MSB หรือ LSB ไว้ที่ address ต่ำ
:::

::: term
[Sign-magnitude]{.abbr} [เครื่องหมายและขนาด]{.th}

- **คืออะไร:** ใช้ MSB เป็นเครื่องหมาย ส่วนบิตที่เหลือเป็นขนาดของตัวเลข เช่น −5 (8 bits) = 1000 0101
- **ข้อเสีย:** มีศูนย์ 2 ตัว (+0, −0) และวงจรบวก/ลบซับซ้อน
:::

::: term
[1's complement]{.abbr} [One's complement]{.full} [ส่วนเติมเต็มหนึ่ง]{.th}

- **คืออะไร:** ทำค่าลบโดย**กลับทุกบิต** เช่น −5 = 1111 1010
- **ข้อเสีย:** ยังมีศูนย์ 2 ตัว และการบวกต้องเอา carry วนกลับมาบวก (end-around carry)
:::

::: term
[2's complement]{.abbr} [Two's complement]{.full} [ส่วนเติมเต็มสอง]{.th}

- **คืออะไร:** วิธีแทนเลขลบที่ใช้ในคอมพิวเตอร์ปัจจุบันเกือบทั้งหมด
- **ทำงานอย่างไร:** −X = **กลับทุกบิตของ X แล้วบวก 1**
  - ทางลัด: เก็บบิตจากขวาไว้จนถึงเลข 1 ตัวแรก แล้วกลับบิตที่เหลือทั้งหมด
  - ตัวอย่าง: +100 = 0110 0100 → 1001 1011 → +1 = **1001 1100 = 0x9C = −100**
- **ข้อดี:** มี**ศูนย์ตัวเดียว** และ**ใช้ adder ตัวเดียวกันได้ทั้งบวกและลบ** (A − B = A + B̄ + 1)
- **ช่วงค่า (n bits):** **−2ⁿ⁻¹ ถึง 2ⁿ⁻¹ − 1** ซึ่ง**ไม่สมมาตร** เช่น 8 bits ได้ −128 ถึง +127
- **สัมพันธ์กับ:** ALU ของ nanoLADA (Ch4) ทำ SUB ด้วยวิธีนี้ ส่วน **sign extension** ใช้ขยายจำนวนบิต
:::

| แบบ (n bits) | ช่วงค่า | ศูนย์ | 8-bit ของ −5 |
|---|---|---|---|
| Unsigned | 0 ถึง 2ⁿ − 1 | 1 ตัว | — |
| Sign-magnitude | −(2ⁿ⁻¹ − 1) ถึง 2ⁿ⁻¹ − 1 | 2 ตัว | 1000 0101 |
| 1's complement | −(2ⁿ⁻¹ − 1) ถึง 2ⁿ⁻¹ − 1 | 2 ตัว | 1111 1010 |
| **2's complement** | **−2ⁿ⁻¹ ถึง 2ⁿ⁻¹ − 1** | **1 ตัว** | **1111 1011** |

::: term
[Sign extension]{.abbr} [การขยายเครื่องหมาย]{.th}

- **คืออะไร:** ขยายเลข 2's complement ให้มีบิตมากขึ้นโดยค่าไม่เปลี่ยน
- **ทำงานอย่างไร:** **คัดลอก sign bit** ไปเติมทางซ้าย เช่น 1001 (−7) → 1111 1001 (−7)
- **สัมพันธ์กับ:** `sign_ext(imm)` ใน nanoLADA (LW/SW/BEQ) ขยาย immediate 16 บิตเป็น 32 บิต ส่วน **zero extension** เติม 0 ใช้กับเลข unsigned
:::

::: term
[Carry vs Overflow]{.abbr} [บิตทด vs ผลล้นช่วง]{.th}

- **Carry out:** บิตที่ทดออกจากหลักซ้ายสุด ซึ่ง**มีความหมายกับเลข unsigned** (ถ้าเป็น 1 แปลว่าผลเกิน 2ⁿ − 1)
- **Overflow (signed):** ผลลัพธ์จริงอยู่นอกช่วงที่ n bits แทนได้
  - เกิดเมื่อ **บวก + บวก ได้ลบ** หรือ **ลบ + ลบ ได้บวก**
  - **บวกเลขต่างเครื่องหมายไม่มีทาง overflow**
  - ฮาร์ดแวร์ตรวจด้วย: **overflow = Cin ของ MSB ⊕ Cout ของ MSB**
:::

::: ex
8 bits: 0x70 + 0x50 = 0111 0000 + 0101 0000 = **1100 0000**
- **carry out = 0**
- แต่บวก + บวก ได้ลบ → **overflow = 1** (112 + 80 = 192 เกิน 127)

8 bits: 0xF0 + 0x20 = (−16) + 32 → ได้ 1 0001 0000
- **carry out = 1**
- ผล 0x10 = 16 ถูกต้อง → **ไม่ overflow**
:::

::: term
[BCD]{.abbr} [Binary-Coded Decimal]{.full} [เลขฐานสิบเข้ารหัสฐานสอง]{.th}

- **คืออะไร:** ใช้ 4 bits แทนเลขฐานสิบ 1 หลัก (0–9) เช่น 59 = 0101 1001
- **ข้อสังเกต:** รหัส 1010–1111 ไม่ได้ใช้ จึงเปลืองบิตกว่า binary ปกติ
:::

::: term
[Gray code]{.abbr} [รหัสเกรย์]{.th}

- **คืออะไร:** รหัสที่ค่าติดกัน**ต่างกันเพียง 1 บิต** เช่นลำดับ 2 บิต: 00, 01, 11, 10
- **ทำงานอย่างไร:** binary → Gray ด้วย g = b ⊕ (b >> 1)
- **สัมพันธ์กับ:** แกนของ **K-map** เรียงตาม Gray code เพื่อให้ช่องที่ติดกันต่างกันแค่ 1 ตัวแปร
:::

## 0.3 Logic Gates และ Boolean Algebra

| Gate | สัญลักษณ์ทางพีชคณิต | Output เป็น 1 เมื่อ |
|---|---|---|
| NOT | A' | A = 0 |
| AND | A·B | ทุกอินพุตเป็น 1 |
| OR | A + B | มีอินพุตอย่างน้อยหนึ่งตัวเป็น 1 |
| NAND | (A·B)' | ไม่ใช่ทุกตัวเป็น 1 |
| NOR | (A + B)' | ทุกตัวเป็น 0 |
| **XOR** | A ⊕ B = A'B + AB' | อินพุต**ต่างกัน** (หรือจำนวน 1 เป็นเลขคี่) |
| **XNOR** | (A ⊕ B)' | อินพุต**เท่ากัน** ใช้ทำ equality comparator |

::: term
[Universal gate]{.abbr} [เกตครอบจักรวาล]{.th}

- **คืออะไร:** gate ชนิดเดียวที่ใช้สร้างฟังก์ชันใดก็ได้ ได้แก่ **NAND** และ **NOR**
- **ทำงานอย่างไร:**
  - NOT A = A NAND A
  - A·B = (A NAND B)' (NAND แล้วกลับด้วย NAND อีกตัว)
  - A + B = A' NAND B'
- **ทำไมสำคัญ:** โรงงานผลิต IC สร้าง gate ชนิดเดียวได้ถูกและเร็ว
:::

### กฎของ Boolean Algebra

| กฎ | แบบ AND | แบบ OR |
|---|---|---|
| Identity | A·1 = A | A + 0 = A |
| Null | A·0 = 0 | A + 1 = 1 |
| Idempotent | A·A = A | A + A = A |
| Complement | A·A' = 0 | A + A' = 1 |
| Absorption | A(A + B) = A | A + AB = A |
| ลดรูป (สำคัญ) | A(A' + B) = AB | **A + A'B = A + B** |
| **DeMorgan** | **(AB)' = A' + B'** | **(A + B)' = A'B'** |
| Distributive | A(B + C) = AB + AC | **A + BC = (A + B)(A + C)** |
| Consensus | AB + A'C + BC = AB + A'C | |

::: key
**DeMorgan: "กลับขีดแล้วสลับเครื่องหมาย"** เติมขีดบนให้แต่ละตัวแปร แล้วเปลี่ยน AND ↔ OR

**Duality:** สลับ AND ↔ OR และ 0 ↔ 1 แล้วสมการยังเป็นจริง
:::

## 0.4 Canonical Forms และ K-map

::: term
[Minterm (m<sub>i</sub>)]{.abbr} [ผลคูณมาตรฐาน]{.th}

- **คืออะไร:** AND ของ**ทุกตัวแปร** (ตัวแปรละครั้ง ในรูปปกติหรือกลับ) ที่ให้ค่า 1 **เพียงแถวเดียว** (แถว i) ของ truth table
- **ทำงานอย่างไร:** แถวไหนบิตเป็น 0 ให้ใช้ตัวกลับ เช่น 3 ตัวแปร m₅ = 101 = **AB'C**
- **สัมพันธ์กับ:** **SOP** F = Σm(แถวที่ F = 1) และ **decoder** (output แต่ละเส้นของ decoder คือ minterm หนึ่งตัว)
:::

::: term
[Maxterm (M<sub>i</sub>)]{.abbr} [ผลบวกมาตรฐาน]{.th}

- **คืออะไร:** OR ของทุกตัวแปรที่ให้ค่า 0 **เพียงแถวเดียว** (แถว i)
- **ทำงานอย่างไร:** แถวไหนบิตเป็น 1 ให้ใช้ตัวกลับ เช่น M₅ = 101 = **A' + B + C'**
- **สัมพันธ์กับ:** **POS** F = ΠM(แถวที่ F = 0)
:::

::: term
[SOP / POS]{.abbr} [Sum of Products / Product of Sums]{.full}

- **SOP:** OR ของ AND terms เช่น F = AB + C' (สร้างจาก**แถวที่เป็น 1**)
- **POS:** AND ของ OR terms เช่น F = (A + B)(C') (สร้างจาก**แถวที่เป็น 0**)
- **ความสัมพันธ์:** Σm กับ ΠM ของฟังก์ชันเดียวกันใช้**เลขแถวที่เหลือกันพอดี** เช่น 3 ตัวแปร Σm(1,3,5) = ΠM(0,2,4,6,7)
- n ตัวแปรมี truth table 2ⁿ แถว และมีฟังก์ชันที่เป็นไปได้ 2^(2ⁿ) ฟังก์ชัน
:::

::: term
[K-map]{.abbr} [Karnaugh map]{.full} [แผนที่คาร์นอห์]{.th}

- **คืออะไร:** ตาราง truth table ที่จัดช่องให้ช่องติดกันต่างกันเพียง 1 ตัวแปร เพื่อใช้ลดรูปสมการด้วยสายตา
- **ทำงานอย่างไร:**
  1. เรียงแกนแบบ **Gray code 00, 01, 11, 10** (ไม่ใช่ 00, 01, 10, 11)
  2. ขอบซ้ายติดกับขอบขวา และขอบบนติดกับขอบล่าง (**wrap around**) ดังนั้น**มุมทั้งสี่ติดกัน**
  3. วงกลุ่มเลข 1 ขนาด 2^k (1, 2, 4, 8, 16) ให้**กลุ่มใหญ่ที่สุดและจำนวนกลุ่มน้อยที่สุด** กลุ่มซ้อนกันได้
  4. ตัวแปรที่ค่าเปลี่ยนภายในกลุ่มจะหายไป
- **สัมพันธ์กับ:** **Don't care**, **prime implicant**, การสร้าง control logic ของ processor
:::

ตำแหน่งเลข minterm ใน K-map 4 ตัวแปร (แถวเป็น AB และคอลัมน์เป็น CD):

| AB \\ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 0 | 1 | 3 | 2 |
| **01** | 4 | 5 | 7 | 6 |
| **11** | 12 | 13 | 15 | 14 |
| **10** | 8 | 9 | 11 | 10 |

::: term
[Don't care (X หรือ d)]{.abbr} [ค่าที่ไม่สนใจ]{.th}

- **คืออะไร:** แถวที่อินพุตนั้นไม่มีทางเกิดขึ้น หรือ output เป็นอะไรก็ได้ (เช่น BCD 1010–1111)
- **ทำงานอย่างไร:** ใน K-map **จะนับเป็น 1 ก็ได้ถ้าช่วยให้กลุ่มใหญ่ขึ้น** หรือ**ไม่ต้องวงก็ได้** (ไม่บังคับให้ครอบ)
- **สัมพันธ์กับ:** ค่า `x` ในตาราง control signals ของ nanoLADA ก็คือ don't care
:::

::: term
[Prime Implicant / Essential PI]{.abbr} [กลุ่มที่ขยายต่อไม่ได้ / กลุ่มที่ต้องเลือก]{.th}

- **Prime implicant:** กลุ่มที่ใหญ่ที่สุดแล้ว ขยายต่อไม่ได้อีก
- **Essential prime implicant:** PI ที่ครอบเลข 1 บางตัวซึ่ง PI อื่นไม่ครอบ จึง**ต้องอยู่ในคำตอบเสมอ**
:::

::: ex
- **Σm(0,2,8,10)** คือ 4 มุม → **B'D'**
- **Σm(0,2,8,10) + d(1,3,9,11)** ครอบทุกช่องที่ B = 0 → **B'** (กลุ่ม 8 ช่องจึงดีกว่า)
- **3 ตัวแปร Σm(0,1,4,5)** ทุกตัวมี B = 0 → **B'**
:::

## 0.5 Combinational Circuits (วงจรเชิงผสม)

::: term
[Combinational circuit]{.abbr} [วงจรเชิงผสม]{.th}

- **คืออะไร:** วงจรที่ output **ขึ้นกับ input ปัจจุบันเท่านั้น** ไม่มีหน่วยความจำ
- **ตัวอย่าง:** MUX, decoder, adder, ALU, comparator
- **สัมพันธ์กับ:** single-cycle processor (Ch4) ทำทุกอย่างของคำสั่งเป็น combinational logic ภายใน 1 cycle ซึ่งตรงข้ามกับ **sequential circuit**
:::

::: term
[MUX]{.abbr} [Multiplexer]{.full} [วงจรเลือกข้อมูล]{.th}

- **คืออะไร:** วงจรที่**เลือก 1 อินพุตจากหลายอินพุต**ส่งออกไปทาง output
- **ทำงานอย่างไร:** MUX **2ⁿ-to-1** มี **select lines n เส้น** เช่น 32-to-1 มี select 5 บิต
  - สมการของ 2-to-1: Y = S'·I₀ + S·I₁
- **ใช้สร้างฟังก์ชัน:** MUX 2ⁿ-to-1 สร้างฟังก์ชัน n ตัวแปรใดก็ได้ (ต่อค่า truth table เข้าที่ data inputs)
- **สัมพันธ์กับ:** ใน datapath ทุกจุดที่ต้อง "เลือก" ใช้ MUX ทั้งหมด เช่น `sel_b` (เลือก R[rt] หรือ imm), `sel_data` (เลือกผล ALU หรือ memory), `sel_wr` (เลือก rd หรือ rt) และ forwarding MUX ใน pipeline
:::

::: term
[DEMUX]{.abbr} [Demultiplexer]{.full}

- **คืออะไร:** ส่งอินพุตเดียวออกไปยัง output 1 จาก 2ⁿ เส้นตาม select (ทำงานกลับด้านกับ MUX)
:::

::: term
[Decoder]{.abbr} [วงจรถอดรหัส]{.th}

- **คืออะไร:** รับอินพุต n บิตแล้วทำให้ output **1 เส้นจาก 2ⁿ เส้น** เป็น 1 (**one-hot**)
- **ทำงานอย่างไร:** output เส้นที่ i = minterm m<sub>i</sub> จึงเอา **decoder + OR gate** สร้าง SOP ใดก็ได้
- **สัมพันธ์กับ:** **register file** ใช้ decoder 5-to-32 เลือก register ที่จะเขียน และ control unit ใช้ decode opcode
:::

::: term
[Encoder / Priority encoder]{.abbr} [วงจรเข้ารหัส]{.th}

- **Encoder:** ทำงานกลับด้านกับ decoder คือแปลงอินพุต one-hot 2ⁿ เส้นเป็นรหัส n บิต
- **Priority encoder:** ถ้ามีหลายอินพุตเป็น 1 พร้อมกัน จะเลือกตัวที่ **priority สูงสุด** (ใช้กับ interrupt หลายแหล่ง)
:::

::: term
[Comparator]{.abbr} [วงจรเปรียบเทียบ]{.th}

- **ทำงานอย่างไร:** เทียบว่าเท่ากันไหมด้วย **XNOR ทุกบิตแล้ว AND รวม**
- **สัมพันธ์กับ:** ใช้เทียบ **tag ใน cache** (n-way ใช้ n comparators) และใน **hazard detection** (rs == rw_ex) ส่วน BEQ ใน nanoLADA ใช้ SUB แล้วดู zero flag
:::

### Adders

::: term
[Half Adder (HA)]{.abbr} [วงจรบวกครึ่ง]{.th}

- **คืออะไร:** บวกเลข 1 บิตสองตัว **ไม่มี carry-in**
- **สมการ:** **S = A ⊕ B** และ **C = A·B**
:::

::: term
[Full Adder (FA)]{.abbr} [วงจรบวกเต็ม]{.th}

- **คืออะไร:** บวก A + B + **Cin** (มี carry-in) เป็นหน่วยพื้นฐานของการบวกหลายบิต
- **สมการ:** **S = A ⊕ B ⊕ Cin** และ **Cout = AB + Cin(A ⊕ B)** = AB + ACin + BCin
- **สัมพันธ์กับ:** สร้างจาก HA 2 ตัว + OR gate และนำไปต่อเป็น ripple-carry adder
:::

::: term
[RCA]{.abbr} [Ripple-Carry Adder]{.full} [วงจรบวกแบบทดต่อเนื่อง]{.th}

- **คืออะไร:** ต่อ FA n ตัวเป็นลูกโซ่ โดย Cout ของบิต i เป็น Cin ของบิต i + 1
- **ข้อเสีย:** carry ต้อง "ไหล" ผ่านทุกบิต delay จึง**แปรตาม n** (เช่น FA ละ 2 gate delays → 16 bits ≈ 32 gate delays)
:::

::: term
[CLA]{.abbr} [Carry-Lookahead Adder]{.full} [วงจรบวกแบบมองล่วงหน้า]{.th}

- **คืออะไร:** adder ที่คำนวณ carry ทุกบิต**พร้อมกัน** ไม่ต้องรอ carry ไหลทีละบิต
- **ทำงานอย่างไร:**
  - **Generate g<sub>i</sub> = A<sub>i</sub>B<sub>i</sub>** (บิตนี้สร้าง carry เอง)
  - **Propagate p<sub>i</sub> = A<sub>i</sub> ⊕ B<sub>i</sub>** (บิตนี้ส่ง carry ต่อ)
  - c<sub>i+1</sub> = g<sub>i</sub> + p<sub>i</sub>c<sub>i</sub> แล้วกระจายสมการให้เหลือแค่ g, p และ c₀
- **Trade-off:** **เร็วกว่าแต่ใช้ gate มากกว่า** (area vs speed)
:::

::: term
[ALU]{.abbr} [Arithmetic Logic Unit]{.full} [หน่วยคำนวณเลขคณิตและตรรกะ]{.th}

- **คืออะไร:** วงจร combinational ที่ทำ operation ทางคณิตศาสตร์ (+, −) และตรรกะ (AND, OR) ตาม **control (alu_ops)**
- **ทำงานอย่างไร:**
  1. ภายในมี adder และ logic unit คำนวณทุกแบบพร้อมกัน แล้ว **MUX เลือกผล**ตาม alu_ops
  2. การลบใช้ **B̄ และ Cin = 1** (2's complement)
  3. **Zero flag = NOR ของทุกบิตของผลลัพธ์** (เป็น 1 เมื่อผลเป็น 0)
- **สัมพันธ์กับ:** nanoLADA ALU มี `00` ADD, `01` OR, `10` SUB และใช้ zero flag กับ BEQ (Ch4) ส่วนในสไลด์ ALU เป็นส่วนที่ช้าที่สุดของ critical path (60 ns)
:::

### Programmable Logic

::: term
[ROM]{.abbr} [Read-Only Memory]{.full} [หน่วยความจำอ่านอย่างเดียว]{.th}

- **ในบริบทวงจร:** ใช้เก็บ truth table ทั้งตาราง โดย address = input และ data = output (2ⁿ แถว)
- **สัมพันธ์กับ:** ใช้ implement control unit และ **microprogram (Map ROM)** ใน Ch5
:::

::: term
[PLA / PAL]{.abbr} [Programmable Logic Array / Programmable Array Logic]{.full}

- **PLA:** มี **AND plane** (สร้าง product terms) และ **OR plane** (รวม terms) ที่ **program ได้ทั้งคู่** จึงประหยัดกว่า ROM เมื่อ product term ใช้ร่วมกันได้
- **PAL:** AND plane program ได้ แต่ **OR plane fixed**
- **สัมพันธ์กับ:** สไลด์ Ch4 สร้าง control ของ nanoLADA ด้วย PLA (G1–G7 คือ AND term ของ opcode แต่ละตัว)
:::

### Timing

::: term
[Propagation delay (t<sub>pd</sub>)]{.abbr} [เวลาหน่วงการแพร่สัญญาณ]{.th}

- **คืออะไร:** เวลาตั้งแต่ input เปลี่ยนจนถึง output นิ่ง
- **สัมพันธ์กับ:** **critical path** คือ path ที่ delay รวมมากที่สุด ซึ่งเป็นตัวกำหนด clock period (เทียบกับ nanoLADA ที่ใช้ 230 ns)
:::

::: term
[Glitch / Hazard (ในวงจร)]{.abbr} [สัญญาณกระพริบ]{.th}

- **คืออะไร:** output เปลี่ยนค่าชั่วคราวผิดพลาด เพราะ path ต่าง ๆ มี delay ไม่เท่ากัน
- **วิธีแก้:** static-1 hazard แก้ได้ด้วยการเพิ่ม consensus term
- **อย่าสับสน:** คำว่า **hazard ใน pipeline (Ch6)** เป็นคนละเรื่องกัน
:::

## 0.6 Sequential Circuits (วงจรเชิงลำดับ)

::: term
[Sequential circuit]{.abbr} [วงจรเชิงลำดับ]{.th}

- **คืออะไร:** วงจรที่ output ขึ้นกับ **input + state (ค่าที่จำไว้)** โดยมีหน่วยความจำ (latch/flip-flop)
- **Synchronous:** state เปลี่ยนเฉพาะที่ขอบ **clock**
- **สัมพันธ์กับ:** register, counter, FSM และ control unit ของ multi-cycle processor (Ch5)
:::

::: term
[Clock]{.abbr} [สัญญาณนาฬิกา]{.th}

- **คืออะไร:** สัญญาณสี่เหลี่ยมที่เป็นจังหวะให้วงจร synchronous
- **ค่าที่เกี่ยวข้อง:** **Clock rate (f)** = จำนวน cycle ต่อวินาที (Hz) และ **Cycle time T<sub>c</sub> = 1/f** เช่น 2 GHz → 0.5 ns
- **สัมพันธ์กับ:** CPU Time = IC × CPI × T<sub>c</sub> (Ch2)
:::

::: term
[Latch vs Flip-flop (FF)]{.abbr} [แลตช์ vs ฟลิปฟล็อป]{.th}

- **Latch:** **level-sensitive** (โปร่งใส ส่งค่าผ่านตลอดช่วงที่ enable = 1)
- **Flip-flop:** **edge-triggered** (รับค่าเฉพาะขอบขาขึ้นหรือขาลงของ clock)
- **สัมพันธ์กับ:** register file (32 × 32 D-FF) และ **pipeline registers** ระหว่าง stage
:::

| FF | Characteristic equation | พฤติกรรม |
|---|---|---|
| **D** (Data/Delay) | **Q⁺ = D** | เก็บค่า D ใช้ทำ register |
| **JK** | **Q⁺ = JQ' + K'Q** | 00 = hold, 01 = reset (0), 10 = set (1), **11 = toggle** |
| **T** (Toggle) | **Q⁺ = T ⊕ Q** | T = 1 → กลับค่า ใช้ทำ counter |
| **SR** (Set-Reset) | Q⁺ = S + R'Q (ต้องมี S·R = 0) | **S = R = 1 ห้ามใช้** |

**Excitation table** (รู้ว่าอยากให้ Q เปลี่ยนเป็นอะไร แล้วต้องป้อนอะไร):

| Q → Q⁺ | D | T | J K | S R |
|---|---|---|---|---|
| 0 → 0 | 0 | 0 | 0 X | 0 X |
| 0 → 1 | 1 | 1 | 1 X | 1 0 |
| 1 → 0 | 0 | 1 | X 1 | 0 1 |
| 1 → 1 | 1 | 0 | X 0 | X 0 |

::: term
[Setup time / Hold time]{.abbr} [เวลาตั้งค่า / เวลาคงค่า]{.th}

- **Setup time:** เวลาที่ input ต้องนิ่ง**ก่อน**ขอบ clock
- **Hold time:** เวลาที่ input ต้องนิ่ง**หลัง**ขอบ clock
- **Clock ขั้นต่ำ:** **T<sub>clk</sub> ≥ t<sub>clk-to-Q</sub> + t<sub>comb,max</sub> + t<sub>setup</sub>**
- **สัมพันธ์กับ:** เป็นเหตุผลที่ pipeline register มี **overhead** ทำให้ pipeline เร็วขึ้นได้ไม่ถึง k เท่าพอดี (Ch6)
:::

::: term
[Register / Shift register]{.abbr} [รีจิสเตอร์]{.th}

- **Register n บิต:** D-FF n ตัวที่ใช้ clock ร่วมกัน (เก็บข้อมูล n บิต)
- **Shift register:** D-FF ต่อกันเป็นลูกโซ่ เลื่อนข้อมูลไปทีละบิตทุก clock (แปลง serial ↔ parallel)
:::

::: term
[Counter]{.abbr} [ตัวนับ]{.th}

- **คืออะไร:** sequential circuit ที่นับเลขตามลำดับ โดย modulo-N ต้องใช้ FF อย่างน้อย **⌈log₂N⌉** ตัว
- **Ripple (asynchronous):** output ของ FF ตัวก่อนเป็น clock ของตัวถัดไป ทำให้ช้าและมี glitch
- **Synchronous:** ทุก FF ใช้ clock เดียวกัน
- **สัมพันธ์กับ:** **PC (Program Counter)** ก็เป็น register ที่เพิ่มค่าทีละ 4
:::

::: term
[FSM]{.abbr} [Finite State Machine]{.full} [เครื่องสถานะจำกัด]{.th}

- **คืออะไร:** แบบจำลองของ sequential circuit ที่มี state จำนวนจำกัด และเปลี่ยน state ตาม input ทุก clock
- **ส่วนประกอบ:** state register (FF) + **next-state logic** + **output logic**
- **ขั้นตอนออกแบบ:**
  1. วาด state diagram
  2. ทำ state table
  3. **state assignment** (กำหนดรหัสบิตให้แต่ละ state)
  4. เลือกชนิด FF
  5. หาสมการด้วย K-map
  6. วาดวงจร
- **จำนวน FF ขั้นต่ำ = ⌈log₂(#states)⌉** เช่น 10 states → 4 FFs ส่วน **one-hot** ใช้ FF เท่ากับจำนวน state (decode ง่ายกว่า)
- **สัมพันธ์กับ:** **control unit ของ multi-cycle processor คือ FSM** (Fetch → Decode → Exec → Mem → WB) (Ch5)
:::

| | **Moore machine** | **Mealy machine** |
|---|---|---|
| Output ขึ้นกับ | **current state เท่านั้น** | **current state + input ปัจจุบัน** |
| เขียน output ไว้ที่ | **ในวงกลม state** | **บนเส้น transition** |
| จำนวน state | มักมากกว่า | มักน้อยกว่า |
| การตอบสนอง | ช้ากว่า 1 clock แต่ output นิ่ง | ทันที แต่อาจ glitch ตาม input |

::: ex
**Sequence detector "101" (overlapping)**
- **Moore: 4 states → 2 FFs**
  - S0 = เริ่มต้น, S1 = เห็น "1", S2 = เห็น "10", S3 = เห็น "101" (output 1)
  - จาก S3: ได้ 0 ไป S2, ได้ 1 ไป S1 (ใช้ "1" ตัวท้ายซ้ำได้)
- **Mealy: 3 states** (S0, S1, S2) โดย output = 1 บนเส้น S2 →(input 1)→ S1
:::

## 0.7 สรุปกับดัก Digital Logic

::: trap
1. **Carry out ≠ overflow:** ต้องดูว่าโจทย์ถาม signed หรือ unsigned
2. **ช่วง 2's complement ไม่สมมาตร:** 8 bits ได้ −128…+127 (และ −(−128) ใน 8 บิตก็ยังได้ −128)
3. **ฐาน 8 ใช้กลุ่มละ 3 บิต ฐาน 16 ใช้กลุ่มละ 4 บิต** และต้องเริ่มจัดกลุ่มจาก**จุดทศนิยม**
4. **แกน K-map เรียง 00, 01, 11, 10** และ**มุมทั้งสี่ติดกัน**
5. **Don't care ไม่บังคับให้วงครอบ**
6. **JK ที่ J = K = 1 คือ toggle** สถานะต้องห้ามเป็นของ **SR**
7. **Moore output อยู่ใน state** ส่วน **Mealy output อยู่บนเส้น**
8. **MUX 2ⁿ-to-1 มี select n เส้น** (32-to-1 มี 5 เส้น ไม่ใช่ 32)
:::
