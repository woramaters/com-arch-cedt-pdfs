# เฉลยละเอียด ชุดที่ 3

## ตารางคำตอบ (ตรวจเร็ว)

| ข้อ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ตอบ | b | a | c | d | a | b | c | b | c | a |
| **ข้อ** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** |
| ตอบ | c | d | b | c | d | c | b | c | a | a |
| **ข้อ** | **21** | **22** | **23** | **24** | **25** | **26** | **27** | **28** | **29** | **30** |
| ตอบ | d | b | c | b | c | a | a | c | c | c |
| **ข้อ** | **31** | **32** | **33** | **34** | **35** | **36** | **37** | **38** | **39** | **40** |
| ตอบ | b | b | c | a | a | b | b | b | c | c |

**แยกคะแนน:** Digital Logic = ข้อ 1–11 + S1–S2 (เต็ม 15) · Computer Architecture = ข้อ 12–40 + S3–S10 (เต็ม 45)

**ข้อไหนอยู่บทไหน** (ใช้หาว่าควรกลับไปอ่านส่วนไหนใน Exam Notes):

| บท | ข้อ |
|---|---|
| Digital Logic | 1–11, S1, S2 |
| Ch1 Introduction | 12, 13 |
| Ch2 Performance | 14–19, S3, S4 |
| Ch3 ISA | 20–25, S5 |
| Ch4 Single cycle | 26–28, S6 |
| Ch5 Multi cycle | 29 |
| Ch6 Pipelining | 30–33, S7 |
| Ch7 ILP | 34, 35 |
| Ch8 Memory | 36–39, S8, S9, S10 |
| Ch9 Storage | 40 |

## Part 1: Choice

### Digital Logic

::: sol
**1. ตอบ [b) 43]{.ans}**

(2B)₁₆ = 2 × 16 + 11 = **43**

- **ตัวลวง a:** ลืมแปลง B (= 11)
- **ตัวลวง d (211):** 0x2B = 0010 1011 อ่านผิดเป็นเลขฐานสิบตรง ๆ
:::

::: sol
**2. ตอบ [a) 11001.101]{.ans}**

- ส่วนจำนวนเต็ม: 25 = 16 + 8 + 1 = **11001**
- ส่วนทศนิยม (คูณ 2 ซ้ำ): 0.625 × 2 = **1**.25 → 0.25 × 2 = **0**.5 → 0.5 × 2 = **1**.0 → อ่านจากบนลงล่างได้ **.101**
- **ตัวลวง b (.011):** อ่านหลักทศนิยมกลับด้าน
:::

::: sol
**3. ตอบ [c) −10]{.ans}**

MSB = 1 จึงเป็นค่าลบ ให้กลับบิตแล้วบวก 1 เพื่อหาขนาด: 0000 1001 + 1 = 0000 1010 = 10 → **−10**

- **ตัวลวง a (−9):** อ่านแบบ 1's complement
- **ตัวลวง b (246):** อ่านแบบ unsigned
- **ตัวลวง d (−118):** อ่านแบบ sign-magnitude
:::

::: sol
**4. ตอบ [d) 1111 1010]{.ans}**

Sign extension = **คัดลอก sign bit (1) ไปเติมทางซ้าย** → 1010 (−6) กลายเป็น 1111 1010 (−6) ค่าเท่าเดิม

- **ตัวลวง a:** zero extension ซึ่งค่าจะเปลี่ยนเป็น +10
- **ตัวลวง c:** กลับบิตแทนการขยาย
:::

::: sol
**5. ตอบ [a) 0x7F + 0x01]{.ans}**

127 + 1 = 128 เกินค่าสูงสุด 127 → ได้ 0x80 (= −128) ซึ่งเป็น**บวก + บวก ได้ลบ** → overflow

- b) −128 + 127 = −1: ต่างเครื่องหมาย ไม่มีทาง overflow
- c) −1 + 1 = 0: มี carry out แต่**ไม่ overflow**
- d) 64 + (−64) = 0: ต่างเครื่องหมาย
:::

::: sol
**6. ตอบ [b) A + B]{.ans}**

กฎ **A + A'B = A + B**
- พิสูจน์: A + A'B = (A + A')(A + B) = 1 · (A + B) ตามกฎ distributive แบบ OR
- **ตัวลวง a:** เป็นกฎ absorption ซึ่งใช้กับ A + AB (ไม่มีขีด)
:::

::: sol
**7. ตอบ [c) C]{.ans}**

m1, m3, m5, m7 = 001, 011, 101, 111 → **C = 1 ทุกตัว** ส่วน A, B เปลี่ยนครบทุกค่า → F = C (เป็นแถวคอลัมน์ C = 1 ทั้งหมดใน K-map)
:::

::: sol
**8. ตอบ [b) ΠM(3, 4, 5, 6, 7)]{.ans}**

POS ใช้**แถวที่ F = 0** คือแถวที่เหลือจาก Σm: {0..7} − {0, 1, 2} = {3, 4, 5, 6, 7}

- **ตัวลวง a:** ใช้เลขเดียวกับ Σm ซึ่งผิด
- **ตัวลวง d:** คือ **F'** ไม่ใช่ F
:::

::: sol
**9. ตอบ [c) Y5]{.ans}**

101₂ = 5 decoder ทำให้ output เส้นที่ 5 เป็น 1 เพียงเส้นเดียว (one-hot) เพราะ Y5 = minterm m5 = AB'C
:::

::: sol
**10. ตอบ [a) 0]{.ans}**

Q⁺ = T ⊕ Q = 1 ⊕ 1 = **0** (T = 1 คือ toggle)
:::

::: sol
**11. ตอบ [c) 12]{.ans}**

**One-hot** ใช้ FF หนึ่งตัวต่อหนึ่ง state ดังนั้น 12 states ใช้ 12 FFs

- **ตัวลวง a (4):** เป็นจำนวนของ **binary encoding** = ⌈log₂12⌉ = 4
- one-hot ใช้ FF มากกว่า แต่ decode state ง่ายกว่า
:::

### Computer Architecture

::: sol
**12. ตอบ [d) Instruction format]{.ans}**

Instruction format เป็นส่วนของ **ISA** (software มองเห็น) ส่วน organization ในสไลด์ประกอบด้วย ALU, Control Unit, Register, Bus, Memory subsystem และ I/O subsystem
:::

::: sol
**13. ตอบ [b)]{.ans}**

สไลด์ Ch1 ใช้ตัวอย่างนี้อธิบาย ISA ในมุม **"abstraction of software for hardware"** คือ hardware รุ่นใหม่ต้องรักษา ISA เดิมไว้ ซอฟต์แวร์เก่าจึงยังรันได้

- **ตัวลวง c:** organization ของ Core i7 ต่างจาก 8088 มาก มีแค่ ISA ที่ compatible กัน
:::

::: sol
**14. ตอบ [c) 2.5]{.ans}**

Speedup = T<sub>old</sub> / T<sub>new</sub> = 10/4 = **2.5**

- **ตัวลวง a:** กลับเศษส่วน
- **ตัวลวง d:** ผลต่าง (10 − 4)
:::

::: sol
**15. ตอบ [d) Toy]{.ans}**

Toy benchmark คือโปรแกรมเล็ก ๆ อย่าง quicksort/merge sort ที่นิยมในอดีต ส่วน synthetic คือโปรแกรมที่เขียนขึ้นให้**เลียนแบบ**พฤติกรรมของโปรแกรมจริง (Whetstone, Dhrystone) และ kernel คือการวัดเฉพาะบางแง่มุมของ performance
:::

::: sol
**16. ตอบ [c) 1 s]{.ans}**

CPU time = IC × CPI / f = (2 × 10⁸ × 2.5) / (5 × 10⁸) = 5 × 10⁸ / 5 × 10⁸ = **1 s**
:::

::: sol
**17. ตอบ [b) 200]{.ans}**

MIPS = f / (CPI × 10⁶) = 500 × 10⁶ / (2.5 × 10⁶) = **200**

ตรวจด้วยอีกสูตร: IC / (T × 10⁶) = 2 × 10⁸ / (1 × 10⁶) = 200 ✓
:::

::: sol
**18. ตอบ [c) 4]{.ans}**

S<sub>max</sub> = 1 / (1 − P) = 1 / 0.25 = **4** เพราะส่วน serial 25% จำกัด speedup (ตัวลวง d ลืม Amdahl)
:::

::: sol
**19. ตอบ [a) Weighted arithmetic mean]{.ans}**

เวลาเป็นค่าที่มีหน่วย และรู้สัดส่วน workload จริง จึงใช้ weighted AM ส่วน geometric mean ใช้กับ **ratio** (speedup) ที่ไม่มีหน่วย
:::

::: sol
**20. ตอบ [a) Memory-Memory (3 operands)]{.ans}**

| แบบ | จำนวนคำสั่ง |
|---|---|
| **Memory-Memory 3-operand** | **4** |
| Memory-Memory 2-operand | 7 |
| Load-Store | 8 |
| Stack / Register-Memory | 10 |
| Accumulator | 11 |

ข้อแลกเปลี่ยนคือ memory traffic สูงมาก
:::

::: sol
**21. ตอบ [d) 0xEF]{.ans}**

Little endian เก็บ **byte ต่ำ (LSB) ไว้ที่ address ต่ำ**: 0x40 = EF, 0x41 = BE, 0x42 = AD, 0x43 = DE

- **ตัวลวง a:** เป็นคำตอบของ big endian
:::

::: sol
**22. ตอบ [b) Memory indirect]{.ans}**

`**p` ต้องอ่าน memory 2 ครั้ง: M[M[R2]] = `LD r1, @(r2)`

- Register indirect = `*p` (อ่านครั้งเดียว)
- Auto-increment = `D[i++]`
:::

::: sol
**23. ตอบ [c)]{.ans}**

Unrestricted alignment: software ง่าย แต่ **hardware ต้องตรวจและแก้ misalignment เอง** มักต้องเข้าถึง memory 2 ครั้งขึ้นไป (ช้า, logic แพง)

- a และ b เป็นลักษณะของ **restricted** alignment
- d ผิด: สไลด์สรุปว่า restricted ชนะในแง่ performance
:::

::: sol
**24. ตอบ [b) Trap]{.ans}**

Exception แบ่งตามแหล่ง: **interrupt** มาจาก hardware ภายนอก ส่วน **trap** มาจาก software (Intel เรียกทั้งสองแบบว่า interrupt)
:::

::: sol
**25. ตอบ [c)]{.ans}**

**Fixed entry:** CPU กระโดดไป address เดิมเสมอ (สไลด์ใช้ 0x1000) แล้วให้ software อ่าน interrupt-source register

- a = vector table
- b = handler table
:::

::: sol
**26. ตอบ [a)]{.ans}**

LW: sel_b = 1 (ใช้ immediate คำนวณ address), sel_data = 1 (เขียนข้อมูลจาก memory), sel_wr = 1 (rt), reg_wr = 1, mem_wr = 0, alu_ops = 00 (ADD)

- **ตัวลวง b:** เป็นค่าของ ADD
- **ตัวลวง c:** เป็นค่าของ SW
- **ตัวลวง d:** เป็นค่าของ JMP
:::

::: sol
**27. ตอบ [a) ORI]{.ans}**

- **ORI → zero extend** (0x0000_imm)
- **ORUI → zero pad** (imm_0000)
- **LW/SW/BEQ → sign extend**
:::

::: sol
**28. ตอบ [c) 0x100]{.ans}**

RTL: PC ← addr × 4 = 0x40 × 4 = **0x100**

- **ตัวลวง a:** ลืมคูณ 4
- **ตัวลวง d:** บวก PC + 4 ซึ่ง JMP ไม่ใช้ (JMP ไม่ได้เป็น PC-relative)
:::

::: sol
**29. ตอบ [c) MEM[REG_S] ← REG_M]{.ans}**

SW 4 cycles:
1. Fetch
2. REG_A ← R[rs], REG_B ← sign_ext(imm), **REG_M ← R[rt]**
3. REG_S ← REG_A + REG_B
4. **MEM[REG_S] ← REG_M**

- **ตัวลวง d:** เป็น write back ซึ่ง SW ไม่มี
:::

::: sol
**30. ตอบ [c) 40]{.ans}**

**ความเร็วของ pipeline ถูกจำกัดด้วย stage ที่ช้าที่สุด** (Lessons learned) ทุก stage ต้องเดินตามจังหวะ 40 นาที จึงเสร็จ 1 load ทุก 40 นาที

- **ตัวลวง d (120):** เป็นผลรวมเวลาของทุกขั้นของผ้า load เดียว (latency) ไม่ใช่อัตราที่ผ้าเสร็จ
:::

::: sol
**31. ตอบ [b)]{.ans}**

Delay slot = คำสั่งหลัง branch ทำงานเสมอ จึงต้องให้ **compiler/software** หาคำสั่งที่ไม่เกี่ยวกับ branch มาใส่ ถ้าหาไม่ได้ต้องใส่ NOP (สไลด์: "Need support from software")
:::

::: sol
**32. ตอบ [b)]{.ans}**

สมการในสไลด์: hazard = (rs = rw<sub>ex</sub> AND regW<sub>ex</sub>) OR (rs = rw<sub>mem</sub> AND regW<sub>mem</sub>) OR (rs = rw<sub>wb</sub> AND regW<sub>wb</sub>) และเงื่อนไขเดียวกันกับ rt คือเทียบ **operand ของคำสั่งปัจจุบัน กับ pending writes**
:::

::: sol
**33. ตอบ [c) Register renaming]{.ans}**

WAR/WAW เป็น **name dependence** (ใช้ชื่อ register ซ้ำ) ถ้าเปลี่ยนให้ใช้ physical register คนละตัวก็หายไป

- **ตัวลวง a:** forwarding แก้ **RAW**
- **ตัวลวง b:** branch prediction แก้ **control hazard**
:::

::: sol
**34. ตอบ [a) IC]{.ans}**

VLIW รวม x operations ใน 1 คำสั่ง → IC = n/x (CPI = 1) ส่วน superscalar ลด **CPI** (1/x) และ superpipeline ลด CPI ที่มีผลด้วย minor cycle
:::

::: sol
**35. ตอบ [a) Intel AVX]{.ans}**

AVX ทำ operation เดียวกับหลายข้อมูลในคำสั่งเดียว (SIMD/vector)

- b = MIMD
- c = SISD
- d = MISD
:::

::: sol
**36. ตอบ [b)]{.ans}**

**Temporal** = ข้อมูลเดิมถูกใช้ซ้ำในเวลาใกล้กัน เช่นตัวแปร i ในทุกรอบของ loop

- a และ c เป็นตัวอย่างของ **spatial** locality (ข้อมูลที่อยู่ติดกัน)
- d เป็นการตั้งค่า cache ที่ใช้ประโยชน์จาก spatial locality
:::

::: sol
**37. ตอบ [b) 128]{.ans}**

#sets = cache size / (block × ways) = 8192 / (32 × 2) = **128**

- **ตัวลวง c (256):** ลืมหารด้วย 2 ways (นั่นคือจำนวน lines)
:::

::: sol
**38. ตอบ [b) Dirty bit]{.ans}**

Write-back เขียนลง memory ตอน replace เท่านั้น จึงต้องมี dirty bit บอกว่า block นี้ถูกแก้ไขแล้ว ถ้า dirty = 0 ตอน replace ไม่ต้องเขียนกลับ
:::

::: sol
**39. ตอบ [c) OS]{.ans}**

Page fault จัดการด้วย **software (OS)** เพราะ hardware ไม่รู้จัก file system หรือ swap ส่วน TLB miss/cache miss เป็นงานของ hardware
:::

::: sol
**40. ตอบ [c) NFS]{.ans}**

NAS ใช้ protocol ระดับไฟล์: **NFS, CIFS/SMB**, AFP, FTP

- **ตัวลวง a:** iSCSI เป็นของ **SAN** (block)
- **ตัวลวง b, d:** Fibre Channel และ SATA เป็น interface ระดับ block
:::

## Part 2: ตอบสั้น

::: sol
**S1. [3 ตัว: A + B = (A' · B')' = NAND(NAND(A,A), NAND(B,B))]{.ans}**

1. NAND ตัวที่ 1: NAND(A, A) = A'
2. NAND ตัวที่ 2: NAND(B, B) = B'
3. NAND ตัวที่ 3: NAND(A', B') = (A'B')' = **A + B** (DeMorgan)

**เกณฑ์:** จำนวนถูก 1 คะแนน และนิพจน์ถูก 1 คะแนน
:::

::: sol
**S2. [F = B'D' + BD]{.ans}** (= B ⊙ D หรือ (B ⊕ D)')

- m0, 2, 8, 10 = 0000, 0010, 1000, 1010 → B = 0 และ D = 0 (4 มุมของ K-map) → **B'D'**
- m5, 7, 13, 15 = 0101, 0111, 1101, 1111 → B = 1 และ D = 1 (สี่เหลี่ยมกลาง) → **BD**

**เกณฑ์:** แต่ละพจน์ 1 คะแนน
:::

::: sol
**S3. [B เร็วกว่า 1.11 เท่า]{.ans}**

IC เท่ากัน จึงเทียบเวลาต่อคำสั่ง = CPI / f
- A: 2.0 / 2 GHz = **1.0 ns**
- B: 2.7 / 3 GHz = **0.9 ns**
- → B เร็วกว่า 1.0/0.9 = **1.11 เท่า**

บทเรียน: clock สูงขึ้น 1.5 เท่า แต่ CPI แย่ลง 1.35 เท่า จึงได้ประโยชน์แค่ 1.11 เท่า
:::

::: sol
**S4. [1.47]{.ans}**

1 / ((1 − 0.4) + 0.4/5) = 1 / (0.6 + 0.08) = 1/0.68 ≈ **1.47**
:::

::: sol
**S5. [(ก) 0x2018 (ข) 0x2180]{.ans}**

- (ก) Vector table: Base + n × address size = 0x2000 + 6 × 4 = 0x2000 + 24 = 0x2000 + **0x18**
- (ข) Handler table: Base + n × handler size = 0x2000 + 6 × 64 = 0x2000 + 384 = 0x2000 + **0x180**

ระวัง: ต้องแปลงผลคูณจากฐานสิบเป็นฐานสิบหกก่อนบวก
:::

::: sol
**S6. [ADD = 190 ns, clock = 230 ns]{.ans}**

- ADD ใช้ PC 10 + Inst MEM 40 + Control 40 + Register 20 + MUX 10 + ALU 60 + MUX 10 = **190 ns** (**ไม่ผ่าน data memory**)
- แต่ single cycle ต้องตั้ง clock ตาม**คำสั่งที่ช้าที่สุด (LW = 230 ns)**
- → ADD เสียเวลาเปล่า 40 ns ต่อคำสั่ง ซึ่งเป็นแรงจูงใจของ multi-cycle
:::

::: sol
**S7. [224 cycles = 448 ns]{.ans}**

- ideal = k + (n − 1) = 5 + 199 = 204 cycles
- load-use = 10% × 200 = 20 ครั้ง ครั้งละ stall 1 cycle → +20
- รวม 224 cycles × 2 ns = **448 ns** (CPI ที่มีผล ≈ 1.12)
:::

::: sol
**S8. [index = 35, tag = 1]{.ans}** (offset = 4)

- offset = log₂16 = 4 bits
- #lines = 4096/16 = 256 → index = 8 bits
- tag = 32 − 8 − 4 = 20 bits

0x1234 = 0001 **0010 0011** 0100:
- offset (4 บิตล่าง) = 0100 = 4
- index (8 บิตถัดไป) = 0010 0011 = 0x23 = **35**
- tag = 0001 = **1**

ตรวจด้วยฐานสิบ: 4660 mod 4096 = 564 → 564 div 16 = 35 ✓ และ 4660 div 4096 = 1 ✓
:::

::: sol
**S9. [CPI = 2.8]{.ans}**

CPI = 1.2 + (1 × 0.01 × 80) + (0.25 × 0.04 × 80) = 1.2 + 0.8 + 0.8 = **2.8**

ทุกคำสั่งต้อง fetch (1 access) แต่มีเพียง 25% ที่มี data access
:::

::: sol
**S10. [VPN = 18 bits, page table = 1 MB]{.ans}**

page 16 KB = 2¹⁴ → offset 14 bits → VPN = 32 − 14 = **18 bits** → 2¹⁸ × 4 B = 2²⁰ B = **1 MB**

ข้อสังเกต: page ใหญ่ขึ้น page table จะเล็กลง (เทียบกับ 4 MB เมื่อ page = 4 KB)
:::

```{=html}
<div class="pagebreak"></div>
```
