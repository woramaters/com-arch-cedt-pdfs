# Digital Logic: สรุปเตรียมสอบ (ส่วน 15 คะแนน)

> **หมายเหตุ:** ไฟล์ PDF ที่ให้มามีแต่ส่วน Computer Architecture **ไม่มีสไลด์ Digital Logic** สรุปนี้จึงอิงเนื้อหามาตรฐานของวิชา Digital Computer Logic (สไลด์ Com Arch อ้างถึงหนังสือ *Contemporary Logic Design* ของ Randy Katz) และเน้นหัวข้อที่ Com Arch หยิบไปใช้ต่อ เช่น MUX, decoder, adder, ALU, PLA, flip-flop และ FSM
> **ถ้ามีสไลด์ Digital Logic ของอาจารย์ ส่งมาได้เลย** จะได้ปรับให้ตรงกับที่สอนจริง

---

## 1. Number Systems

### 1.1 การแปลงฐาน
- **ฐานใดก็ได้ → ฐาน 10:** คูณแต่ละหลักด้วยค่าประจำหลัก เช่น (1011.01)₂ = 8 + 2 + 1 + 0.25 = **11.25**
- **ฐาน 10 → ฐาน 2:**
  - ส่วนจำนวนเต็ม: หาร 2 ไปเรื่อย ๆ แล้วอ่านเศษ**จากล่างขึ้นบน**
  - ส่วนทศนิยม: คูณ 2 ไปเรื่อย ๆ แล้วอ่านหลักหน้าจุด**จากบนลงล่าง**
- **ฐาน 2 ↔ 16:** จัดกลุ่มทีละ **4** บิต
- **ฐาน 2 ↔ 8:** จัดกลุ่มทีละ **3** บิต (เริ่มจากจุดทศนิยม)
  - ตัวอย่าง: 0x3F7 = 0011 1111 0111 → 001 111 110 111 = **1767₈**

| Dec | Bin | Hex | | Dec | Bin | Hex |
|---|---|---|---|---|---|---|
| 0 | 0000 | 0 | | 8 | 1000 | 8 |
| 1 | 0001 | 1 | | 9 | 1001 | 9 |
| 2 | 0010 | 2 | | 10 | 1010 | A |
| 3 | 0011 | 3 | | 11 | 1011 | B |
| 4 | 0100 | 4 | | 12 | 1100 | C |
| 5 | 0101 | 5 | | 13 | 1101 | D |
| 6 | 0110 | 6 | | 14 | 1110 | E |
| 7 | 0111 | 7 | | 15 | 1111 | F |

### 1.2 Signed Numbers (n bits)

| แบบ | วิธีทำค่าลบ | ช่วงค่า | ศูนย์ |
|---|---|---|---|
| Sign-magnitude | เปลี่ยน bit ซ้ายสุดเป็น 1 | −(2ⁿ⁻¹−1) ถึง 2ⁿ⁻¹−1 | มี 2 ตัว (+0, −0) |
| 1's complement | กลับทุกบิต | −(2ⁿ⁻¹−1) ถึง 2ⁿ⁻¹−1 | มี 2 ตัว |
| **2's complement** | **กลับทุกบิตแล้วบวก 1** | **−2ⁿ⁻¹ ถึง 2ⁿ⁻¹−1** | มีตัวเดียว |
| Unsigned | — | 0 ถึง 2ⁿ−1 | |

- ตัวอย่าง 8-bit: +100 = 0110 0100 → −100 = 1001 1011 + 1 = **1001 1100 = 0x9C**
- ทางลัด: เก็บบิตจากขวาไว้จนถึง 1 ตัวแรก แล้วกลับบิตที่เหลือทั้งหมด
- **Sign extension:** ขยายจำนวนบิตโดยก๊อป sign bit ไปข้างหน้า เช่น 1001 (−7) → 1111 1001 (ตรงกับ `sign_ext` ใน nanoLADA)
- **การลบ:** A − B = A + (B̄ + 1) ALU จึงใช้ adder ตัวเดียวทำได้ทั้งบวกและลบ (กลับบิต B แล้วให้ carry-in = 1)

### 1.3 Overflow vs Carry ⚠️
- **Carry out** = มีบิตล้นออกจากบิตซ้ายสุด ซึ่ง**มีความหมายกับ unsigned**
- **Signed overflow** เกิดเมื่อ **บวก + บวก ได้ลบ** หรือ **ลบ + ลบ ได้บวก**
  - วิธีเช็คด้วย hardware: overflow = **C_in ของ MSB ⊕ C_out ของ MSB**
  - **บวกเลขต่างเครื่องหมายไม่มีทาง overflow**
- ตัวอย่าง 8-bit: 0x70 + 0x50 = 112 + 80 = 192 ได้ผล 0xC0 = 1100 0000 → **carry out = 0 แต่ signed overflow = 1** (ผลอ่านได้เป็น −64)
- ตัวอย่าง 8-bit: 0xF0 + 0x20 = (−16) + 32 = 16 → **carry out = 1 แต่ไม่ overflow** (ผล 0x10 ถูกต้อง)

### 1.4 Codes อื่นที่อาจออก
- **BCD:** แต่ละหลักฐานสิบใช้ 4 บิต เช่น 59 = 0101 1001
- **Gray code:** ค่าที่อยู่ติดกันต่างกันเพียง 1 บิต
  - Binary → Gray: g = b ⊕ (b >> 1)
  - ลำดับ 2 บิต: 00, 01, 11, 10 (ลำดับเดียวกับแกนของ K-map)

---

## 2. Boolean Algebra

| กฎ | AND form | OR form |
|---|---|---|
| Identity | A·1 = A | A + 0 = A |
| Null | A·0 = 0 | A + 1 = 1 |
| Idempotent | A·A = A | A + A = A |
| Complement | A·A' = 0 | A + A' = 1 |
| **Absorption** | A(A + B) = A | A + AB = A |
| ลดรูป | A(A' + B) = AB | **A + A'B = A + B** |
| **DeMorgan** | **(AB)' = A' + B'** | **(A + B)' = A'B'** |
| Distributive | A(B + C) = AB + AC | **A + BC = (A + B)(A + C)** |
| **Consensus** | AB + A'C + BC = AB + A'C | |

- **XOR:** A ⊕ B = A'B + AB' (เป็น 1 เมื่ออินพุตต่างกัน) และ **XNOR** = (A ⊕ B)' (เป็น 1 เมื่อเท่ากัน ใช้เป็น equality comparator)
- **Universal gates:** **NAND** อย่างเดียว (หรือ **NOR** อย่างเดียว) สร้างวงจรได้ทุกฟังก์ชัน
  - NOT A = A NAND A
  - A·B = (A NAND B) NAND (A NAND B)
  - A + B = A' NAND B'
- **Duality:** สลับ AND↔OR และ 0↔1 แล้วสมการยังเป็นจริง

### 2.1 Canonical Forms
- **Minterm** m_i = AND term ที่ให้ 1 เฉพาะแถว i เช่น 3 ตัวแปร m₅ = AB'C (101)
- **Maxterm** M_i = OR term ที่ให้ 0 เฉพาะแถว i เช่น M₅ = A' + B + C'
- **SOP:** F = Σm(...) (ใช้แถวที่ F = 1) ส่วน **POS:** F = ΠM(...) (ใช้แถวที่ F = 0)
- Σm กับ ΠM ของฟังก์ชันเดียวกัน**ใช้เลขแถวที่เหลือกันพอดี** เช่น 3 ตัวแปร Σm(1,3,5) = ΠM(0,2,4,6,7)
- n ตัวแปรมี **2^(2ⁿ)** ฟังก์ชันที่เป็นไปได้ เช่น 2 ตัวแปรมี 16 ฟังก์ชัน

---

## 3. K-map Minimization

- เรียงแกนตาม **Gray code** (00, 01, 11, 10) และ**ขอบซ้าย-ขวา/บน-ล่างถือว่าติดกัน (wrap around)**
- วงกลุ่มขนาด **2^k** (1, 2, 4, 8, 16) ให้**ใหญ่ที่สุด**และ**น้อยกลุ่มที่สุด** กลุ่มซ้อนกันได้
- **Don't care (d หรือ X):** เอามารวมในกลุ่มได้ถ้าช่วยให้กลุ่มใหญ่ขึ้น ไม่บังคับให้ครอบ
- **Prime implicant** = กลุ่มที่ขยายต่อไม่ได้แล้ว ส่วน **Essential PI** = PI ที่ครอบ 1 บางตัวที่ PI อื่นไม่ครอบ (ต้องเลือกเสมอ)

ลำดับช่องของ K-map 4 ตัวแปร (แถวเป็น AB และคอลัมน์เป็น CD):
```
        CD=00 01  11  10
AB=00     0   1   3   2
AB=01     4   5   7   6
AB=11    12  13  15  14
AB=10     8   9  11  10
```
- ตัวอย่าง: F = Σm(0,2,8,10) คือ **4 มุม** → **B'D'**
- ถ้าเพิ่ม d(1,3,9,11) จะครอบทั้ง**แถวที่ B = 0** → **F = B'**
- ตัวอย่าง: F = Σm(0,1,4,5) (3 ตัวแปร ABC) → B = 0 ทั้งหมด → **B'**

---

## 4. Combinational Circuits

| วงจร | หน้าที่ | ขนาด |
|---|---|---|
| **MUX 2ⁿ-to-1** | เลือก 1 จาก 2ⁿ อินพุตด้วย **n select lines** | 32-to-1 ใช้ 5 select bits |
| **Decoder n-to-2ⁿ** | อินพุต n บิตเลือก output 1 เส้น (one-hot) แต่ละ output คือ minterm หนึ่งตัว | 5-to-32 ใช้เลือก register ใน register file |
| **Encoder / Priority encoder** | กลับด้านของ decoder ส่วน priority encoder เลือกอินพุตที่ priority สูงสุด | |
| **Demux** | ส่งอินพุตเดียวไปยัง output ที่เลือก | |
| **Comparator** | เทียบเท่ากันด้วย XNOR ทุกบิตแล้ว AND รวม | BEQ ใช้ SUB แล้วเช็ค zero |

- **MUX สร้างฟังก์ชันใดก็ได้:** MUX 2ⁿ-to-1 ทำฟังก์ชัน n ตัวแปรได้ (ต่อค่า truth table เข้าที่ data inputs) หรือใช้ MUX 2ⁿ⁻¹-to-1 กับตัวแปรสุดท้ายที่ data inputs (0, 1, x, x')
- **Decoder + OR gate** สร้าง SOP ใดก็ได้ (OR minterm ที่ต้องการเข้าด้วยกัน)

### 4.1 Adders
- **Half adder:** S = A ⊕ B, C = AB
- **Full adder:** **S = A ⊕ B ⊕ Cin** และ **Cout = AB + Cin(A ⊕ B)** (= AB + ACin + BCin)
- **Ripple-carry adder (n bits):** ต่อ full adder n ตัวเป็นลูกโซ่ delay ∝ **n** (carry ต้องวิ่งผ่านทุกบิต)
  - ถ้า carry ผ่านหนึ่ง FA ใช้ 2 gate delays → 16-bit ใช้ประมาณ **32 gate delays**
- **Carry-lookahead adder:** ใช้ **Generate gᵢ = AᵢBᵢ** และ **Propagate pᵢ = Aᵢ ⊕ Bᵢ** แล้วคำนวณ cᵢ₊₁ = gᵢ + pᵢcᵢ แบบขนาน → เร็วกว่าแต่ใช้ gate มากกว่า (trade-off ระหว่าง area กับ speed)
- **ALU:** adder + logic unit + MUX เลือกผลลัพธ์ (ตาม `alu_ops` ใน nanoLADA) การลบใช้ B̄ และ Cin = 1 ส่วน **zero flag = NOR ของทุกบิตของผล**

### 4.2 ROM / PLA (ใช้สร้าง control unit ใน Com Arch)
- **ROM:** address = อินพุต และ data = output → เก็บ truth table ทั้งตาราง (2ⁿ แถว)
- **PLA:** **AND plane** (สร้าง product terms) + **OR plane** (รวม terms) ที่ program ได้ทั้งสองระนาบ จึงประหยัดกว่า ROM เมื่อ product term ใช้ร่วมกันได้ (ตัวอย่าง G1–G7 ของ nanoLADA)
- **PAL:** AND plane program ได้ แต่ OR plane fixed

### 4.3 Timing
- **Propagation delay:** เวลาจาก input เปลี่ยนจนถึง output นิ่ง
- **Critical path:** path ที่ delay รวมยาวที่สุด ซึ่งเป็นตัวกำหนด clock period (เทียบกับ single-cycle nanoLADA = 230 ns)
- **Hazard/glitch** ในวงจร combinational: output กระพริบชั่วคราวเพราะ path มี delay ต่างกัน
  - Static-1 hazard แก้ได้ด้วยการเพิ่ม consensus term

---

## 5. Sequential Circuits

### 5.1 Latch vs Flip-flop
- **Latch:** level-sensitive (โปร่งใสตลอดช่วงที่ enable = 1)
- **Flip-flop:** **edge-triggered** (เปลี่ยนเฉพาะขอบ clock)
- **SR latch:** S = R = 1 เป็นสถานะต้องห้าม (สำหรับแบบ NOR)

| FF | Characteristic equation | พฤติกรรม |
|---|---|---|
| **D** | **Q⁺ = D** | ใช้ทำ register (register file คือ D-FF 32×32) |
| **JK** | **Q⁺ = JQ' + K'Q** | 00 = hold, 01 = reset, 10 = set, **11 = toggle** |
| **T** | **Q⁺ = T ⊕ Q** | T = 1 → toggle (ใช้ทำ counter) |
| SR | Q⁺ = S + R'Q (SR = 0) | 11 = ห้าม |

**Excitation table** (รู้ Q → Q⁺ แล้วถามว่าต้องป้อนอะไร):

| Q→Q⁺ | D | T | J K |
|---|---|---|---|
| 0→0 | 0 | 0 | 0 X |
| 0→1 | 1 | 1 | 1 X |
| 1→0 | 0 | 1 | X 1 |
| 1→1 | 1 | 0 | X 0 |

- **Setup time** = เวลาที่ D ต้องนิ่ง**ก่อน**ขอบ clock ส่วน **hold time** = เวลาที่ต้องนิ่ง**หลัง**ขอบ clock
- ช่วงเวลา clock ขั้นต่ำ: **T_clk ≥ t_clk-to-Q + t_comb(max) + t_setup** (เหตุผลเดียวกับที่ pipeline register มี overhead)

### 5.2 Registers & Counters
- **Register n บิต** = D-FF n ตัว ส่วน **shift register** = D-FF ต่อกันเป็นลูกโซ่
- **Counter:** modulo-N ใช้ FF อย่างน้อย **⌈log₂N⌉** ตัว
  - **Ripple (asynchronous) counter:** ใช้ output ของ FF ตัวก่อนเป็น clock ของตัวถัดไป จึงช้าและมี glitch
  - **Synchronous counter:** ทุก FF ใช้ clock เดียวกัน

### 5.3 Finite State Machine (FSM)

| | **Moore** | **Mealy** |
|---|---|---|
| Output ขึ้นกับ | **current state อย่างเดียว** | **current state + input** |
| จำนวน state | มักมากกว่า | มักน้อยกว่า |
| Output ตอบสนอง | ช้ากว่า 1 clock แต่ไม่ glitch | ทันที แต่อาจ glitch ตาม input |

- **จำนวน FF ขั้นต่ำ = ⌈log₂(#states)⌉** เช่น 10 states → 4 FFs (binary encoding) ส่วน **one-hot** ใช้ FF เท่ากับจำนวน state (decode ง่าย)
- **ขั้นตอนออกแบบ:**
  1. state diagram
  2. state table
  3. **state assignment** (กำหนดรหัสให้ state)
  4. เลือกชนิด FF
  5. หา next-state logic และ output logic ด้วย K-map
  6. วาดวงจร
- **ตัวอย่าง: sequence detector "101" แบบ overlapping**
  - **Moore: 4 states** (S0 = ไม่มีอะไร, S1 = "1", S2 = "10", S3 = "101" → output 1) ใช้ **2 FFs**
  - **Mealy: 3 states** (S0, S1, S2) โดย output = 1 บน transition S2 →(1)→ S1
- **เชื่อมกับ Com Arch:** control unit ของ **multi-cycle processor คือ FSM** (Fetch → Decode → Exec → …) ซึ่ง implement ได้ด้วย sequential circuit (state assignment + next-state truth table) หรือ **microprogram (ROM)**

---

## ⚠️ กับดัก Digital Logic

1. **Carry out ≠ overflow** ต้องดูว่าโจทย์ถาม signed หรือ unsigned
2. **ช่วง 2's complement ไม่สมมาตร:** 8 บิตได้ −128…+127 (และ −(−128) ใน 8 บิตก็ยังได้ −128)
3. **ฐาน 8 จัดกลุ่ม 3 บิต ฐาน 16 จัดกลุ่ม 4 บิต** และต้องเริ่มจัดจาก**จุดทศนิยม**
4. **แกน K-map เรียง 00, 01, 11, 10** ไม่ใช่ 00, 01, 10, 11 และอย่าลืมว่า**มุมทั้งสี่ติดกัน**
5. **Don't care ไม่จำเป็นต้องวงครอบ** ให้ใช้เฉพาะเมื่อทำให้กลุ่มใหญ่ขึ้น
6. **JK กับ J = K = 1 คือ toggle** ไม่ใช่สถานะต้องห้าม (ต้องห้ามเป็นของ **SR**)
7. **Moore output อยู่ใน state** ส่วน **Mealy output อยู่บนเส้น transition**
8. **MUX 2ⁿ-to-1 มี select n เส้น** ไม่ใช่ 2ⁿ
