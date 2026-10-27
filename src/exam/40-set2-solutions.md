# เฉลยละเอียด ชุดที่ 2

## Part A: เติมคำ

| # | คำตอบ | อธิบาย |
|---|---|---|
| 1 | **software, hardware** | ISA คือสัญญาระหว่าง SW กับ HW |
| 2 | **IBM 360** (System/360) | ก่อนหน้านั้นโปรแกรมไม่ portable |
| 3 | **Organization** (microarchitecture) | ต่างกันที่จำนวน core, cache, Turbo Boost, Hyper-Threading |
| 4 | **Synthetic** | เขียนขึ้นให้เลียนแบบโปรแกรมจริง |
| 5 | **Geometric** | ratio ไม่มีหน่วย และ GM ให้ผล consistent กับทุก baseline |
| 6 | **0x12** | little endian: 0x200 = 34, **0x201 = 12**, 0x202 = FE, 0x203 = CA |
| 7 | **A mod s** | |
| 8 | **Auto-increment**, `D[i++]` | อ่าน M[R2] แล้วเพิ่ม R2 |
| 9 | **16**, **26** | I: 6 + 5 + 5 + 16 และ J: 6 + 26 |
| 10 | **Zero pad**, **Sign extend** | ORUI ให้ imm ไปอยู่ 16 บิตบน (ส่วน ORI ใช้ zero extend) |
| 11 | **LW** | 10 + 40 + 40 + 20 + 10 + 60 + 40 + 10 = 230 ns |
| 12 | **5, 4, 3** | |
| 13 | **FSM (Finite State Machine)**, **Microprogram** | |
| 14 | **WAR** | i เขียนสิ่งที่ j อ่าน |
| 15 | **SIMD**, **MIMD** | |
| 16 | **Hyper-Threading** | |
| 17 | **DRAM**, **SRAM** | |
| 18 | **Conflict** | แก้ด้วย associativity |
| 19 | **Page fault**, write-**back** | write-through ไปดิสก์แพงเกินไป |
| 20 | **6**, **3** | |

## Part B: ปรนัย

::: sol
**B1. [c)]{.ans}** จำนวน cache level เป็นเรื่องของ **organization** ซึ่ง software มองไม่เห็นผ่าน ISA ส่วน a, b, d ล้วนเป็นสิ่งที่ ISA กำหนด (format, addressing mode, interrupt handling)
:::

::: sol
**B2. [b)]{.ans}**

- T<sub>A</sub> = 8 × 10⁸ / (400 × 10⁶) = **2 s**
- T<sub>B</sub> = 5 × 10⁸ / (300 × 10⁶) = **1.67 s**
- → B เร็วกว่า 2 / 1.67 = **1.2 เท่า**

ไม่ต้องรู้ clock rate เพราะ MIPS รวมไว้แล้ว (ตัวลวง d) และนี่คือเหตุผลที่ **MIPS ใช้เทียบข้าม ISA ไม่ได้**
:::

::: sol
**B3. [d)]{.ans}** Load-store มี fixed-length format และ CPI ใกล้เคียงกันทุกคำสั่ง จึงจัด stage ได้สม่ำเสมอ ส่วนแบบอื่นมี bottleneck (ACC, stack) หรือ CPI แปรผัน (memory-memory)
:::

::: sol
**B4. [b)]{.ans}** Stack มีข้อดีคือ code density ดีและ compiler ง่าย (ตัวลวง a, d กลับกัน) แต่มีข้อเสียคือข้อมูลที่ต้องการไม่ได้อยู่ top of stack เสมอ และ stack เป็น bottleneck
:::

::: sol
**B5. [b)]{.ans}** การเทียบมาก/น้อยดูจาก byte สูง (มี sign bit) ก่อน ซึ่ง big endian เก็บ byte สูงไว้ที่ address ต่ำ จึงอ่านได้ก่อนและตอบได้ทันที ส่วน little endian เหมาะกับ**การบวก** (ส่ง carry จาก byte ต่ำขึ้นไป)
:::

::: sol
**B6. [b) 0x8014]{.ans}**

0x8000 + 5 × 4 = 0x8000 + 20 = 0x8000 + **0x14**

- **ตัวลวง a:** ลืมคูณขนาด
- **ตัวลวง c (0x8050):** เป็นคำตอบของ handler table ขนาด 16 B
:::

::: sol
**B7. [d)]{.ans}** XOR R1,R1,R1 ไม่ต้องมี immediate ทำให้ encode สั้น และ HW ส่วนใหญ่รู้จัก idiom นี้ (สไลด์: "For most architecture, the recommended method is XOR")
:::

::: sol
**B8. [b)]{.ans}** **Code motion** คือย้ายโค้ดที่ไม่เปลี่ยนค่าใน loop (loop-invariant) ออกนอก loop เป็น global optimization ส่วน strength reduction คือใช้ operation ที่ถูกกว่า (เช่น shift แทนคูณ)
:::

::: sol
**B9. [b) SW]{.ans}** SW เป็นคำสั่งเดียวที่เขียน memory (mem_wr = 1) และไม่เขียน register (reg_wr = 0)
:::

::: sol
**B10. [c) 0xBEEF0000]{.ans}** ORUI ใช้ **zero_pad** ซึ่งให้ imm ไปอยู่ 16 บิตบน แล้ว OR กับ r0 (= 0) ได้ 0xBEEF0000

- **ตัวลวง a:** zero extend (ORI)
- **ตัวลวง b:** sign extend
:::

::: sol
**B11. [b) 0x0038]{.ans}**

PC + 4 = 0x44 แล้วบวก sign_ext(−3) × 4 = −12 = −0xC → 0x44 − 0xC = **0x38**

- **ตัวลวง a:** ลืมบวก 4
- **ตัวลวง c:** ลืมคูณ imm ด้วย 4
:::

::: sol
**B12. [b) ≤ 4]{.ans}** เวลาต่อคำสั่งต้องไม่มากกว่าเดิม: CPI × 60 ≤ 240 → **CPI ≤ 4** (แบบเดียวกับตัวอย่างในสไลด์ 210/45 ≈ 4.67)
:::

::: sol
**B13. [b)]{.ans}**

- ตัวลวง a ผิด (pipeline **ไม่ลด latency**)
- c ผิด (fill/drain และ hazard ทำให้ไม่ถึง k พอดี)
- d ผิด (stage ที่ไม่สมดุลทำให้ speedup ลดลง)
:::

::: sol
**B14. [a) Structural]{.ans}** ถ้ามี memory ตัวเดียว คำสั่งหนึ่ง fetch (IF) พร้อมกับอีกคำสั่งหนึ่งอ่านหรือเขียนข้อมูล (MEM) ได้ไม่ได้ เป็นการแย่ง resource → แก้ด้วยการเพิ่ม resource (แยก I-cache กับ D-cache)
:::

::: sol
**B15. [b)]{.ans}**

**Load-use:** LW ได้ข้อมูลตอนจบ MEM แต่ ADD ต้องใช้ตอนต้น EX ใน cycle เดียวกัน → ต้อง stall 1 cycle ("ต้องมีไทม์แมชชีน")

- a และ d: ผล ALU พร้อมตอนจบ EX จึง forward ได้ทัน
- c: ไม่มี dependency
:::

::: sol
**B16. [b)]{.ans}** delay slot คือนิยามใหม่ว่าคำสั่งหลัง branch ทำงานเสมอ ซึ่ง**ต้องอาศัย compiler** หาคำสั่งมาใส่ (ตัวลวง d ผิด) และไม่ใช่ branch prediction (ตัวลวง c)
:::

::: sol
**B17. [b) 504]{.ans}**

T = (k + (n − x)/x) = 5 + 998/2 = 5 + 499 = **504 T<sub>c</sub>**

- **ตัวลวง a (1004):** pipeline ธรรมดา (5 + 999)
- speedup เทียบ pipeline ≈ 1004/504 ≈ 2 = x
:::

::: sol
**B18. [c)]{.ans}**

- VLIW ใช้ **static scheduling** (ตัวลวง a ผิด)
- VLIW **ลด IC** (n → n/x) โดย CPI = 1 (ตัวลวง b กลับกัน)
- Intel ประกาศ EOL ของ Itanium ในปี 2019 (ตัวลวง d ผิด)
:::

::: sol
**B19. [b)]{.ans}**

- Associativity ลด **conflict miss** แต่ต้องมี comparator n ตัวและ MUX ใหญ่ขึ้น จึง**อาจเพิ่ม hit time**
- compulsory miss ไม่ได้ลดลง (ตัวลวง a)
- capacity miss ไม่เป็นศูนย์ (ตัวลวง c)
- ยังต้องมี tag (ตัวลวง d)
:::

::: sol
**B20. [a) Block, File]{.ans}** EBS = block storage (เหมือนดิสก์เปล่าให้ VM) ส่วน NAS/NFS = file storage
:::

## Part C: คำนวณและอธิบาย

::: sol
**C1 (8 คะแนน)**

**(a)**
- CPI = 0.5(1) + 0.2(5) + 0.1(4) + 0.2(3) = 0.5 + 1.0 + 0.4 + 0.6 = [**2.5**]{.ans} (1.5)
- CPU time = 10⁹ × 2.5 / (2.5 × 10⁹) = [**1.0 s**]{.ans} (1.5)

**(b)**
- CPI<sub>ใหม่</sub> = 0.5 + 0.2(3) + 0.4 + 0.6 = **2.1**
- Speedup = 2.5 / 2.1 = [**1.19**]{.ans} (2) (IC และ clock เท่าเดิมจึงตัดทิ้งได้)

**(c)**
- Amdahl ต้องใช้ **P = สัดส่วนของเวลา** ที่ใช้กับ load (1)
- เวลาของ load = 0.2 × 5 = 1.0 จาก 2.5 → **P = 0.4** (1)
- n = 5/3 → 1 / (0.6 + 0.4 × 3/5) = 1 / (0.6 + 0.24) = 1/0.84 = **1.19** ✓ (1)
- ถ้าใช้ P = 0.2 จะได้ 1/(0.8 + 0.12) = 1.087 ซึ่ง**ผิด** เพราะ load แต่ละคำสั่งใช้เวลามากกว่าคำสั่งเฉลี่ย สัดส่วนของ**คำสั่ง**จึงไม่เท่ากับสัดส่วนของ**เวลา**
:::

::: sol
**C2 (5 คะแนน)**

- **(a)** 1 / (0.3 + 0.7/8) = 1/0.3875 = [**2.58**]{.ans} (2)
- **(b)** 1/0.3 = [**3.33**]{.ans} (1)
- **(c)** (2)
  - (i) 64 cores: 1 / (0.3 + 0.7/64) = 1/0.3109 = **3.22**
  - (ii) serial เร็วขึ้น 2 เท่า: 1 / (0.15 + 0.0875) = 1/0.2375 = **4.21**
  - → [**(ii) ดีกว่า**]{.ans} เพราะส่วน serial เป็นตัวจำกัด speedup (Amdahl) การเพิ่ม core ให้ผลลดลงเรื่อย ๆ (diminishing returns)
:::

::: sol
**C3 (9 คะแนน)**

**(a)** single cycle มี CPI = 1: 7 × 230 = [**1610 ns**]{.ans} (2)

**(b)** (3)

| คำสั่ง | LW | LW | ADD | ORI | SW | BEQ | JMP | รวม |
|---|---|---|---|---|---|---|---|---|
| Cycles | 5 | 5 | 4 | 4 | 4 | 3 | 3 | **28** |

28 × 50 = [**1400 ns**]{.ans} (CPI เฉลี่ย = 4.0 → เร็วกว่า single เพียง 1.15 เท่า)

**(c)** (2)
- (k + n − 1) × T<sub>c</sub> = (5 + 7 − 1) × 50 = [**550 ns**]{.ans}
- speedup = 1610/550 = [**2.93**]{.ans}
- ไม่ถึง 5 เพราะ n น้อย (เวลา fill มีผลมาก) และ 5 stages × 50 = 250 ns > 230 ns

**(d)** ตอบอย่างน้อย 2 ข้อ (2)
- **RAW (load-use)** บน r2: LW#2 → ADD (r1 จาก LW#1 ห่าง 2 คำสั่ง forward ได้)
- **RAW** บน r3: ADD → ORI
- **RAW** บน r4: ORI → SW
- **Control hazard:** BEQ และ JMP
:::

::: sol
**C4 (10 คะแนน)**

**(a)** (3)
- offset = log₂32 = [**5 bits**]{.ans}
- #lines = 16 KB / 32 B = 512 → index = [**9 bits**]{.ans}
- tag = 32 − 9 − 5 = [**18 bits**]{.ans}

**(b)** 0x00012345 = 74,565 (3)
- **offset** = 74,565 mod 32 = [**5**]{.ans}
- **index** = (74,565 mod 16,384) div 32 = 9,029 div 32 = [**282**]{.ans}
- **tag** = 74,565 div 16,384 = [**4**]{.ans}
- ตรวจด้วย binary: 0x12345 = `0001 0010 0011 0100 0101` → 5 บิตล่าง = 00101 = 5, 9 บิตถัดไป = 1 0001 1010 = 0x11A = 282, ที่เหลือ = 0100 = 4 ✓

**(c)** (2)
- 0x16345 = 0x12345 + 0x4000 (+16,384 = **ขนาด cache พอดี**)
- index = 282 และ offset = 5 **เท่าเดิม** แต่ tag = 5 ≠ 4
- → อยู่ line เดียวกันแต่ tag ต่างกัน = [**conflict miss**]{.ans} ถ้าใช้สลับกันจะไล่กันออกไปมา (ping-pong)

**(d)** (2)
- #sets = 512/2 = 256 → [**offset 5, index 8, tag 19**]{.ans}
- ใช้ [**2 comparators**]{.ans} (หนึ่งตัวต่อ way)
- ทั้งสอง address อยู่ set 282 mod 256 = 26 ได้พร้อมกัน → conflict หายไป
:::

::: sol
**C5 (6 คะแนน)**

**(a)** (3)
- ทุกคำสั่งต้อง fetch 1 ครั้ง และ 30% มี data access เพิ่ม
- CPI = 1 + 1 × 0.02 × 100 + 0.3 × 0.05 × 100 = 1 + 2 + 1.5 = [**4.5**]{.ans}
- → ช้ากว่า perfect cache [**4.5 เท่า**]{.ans} (memory stall กินเวลา 3.5/4.5 ≈ 78%)

**(b)** (3)
- MissPenalty<sub>L1</sub> = 10 + 0.2 × 100 = 30 cycles
- AMAT = 1 + 0.05 × 30 = [**2.5 cycles**]{.ans}
- ถ้าไม่มี L2 จะได้ 1 + 0.05 × 100 = 6 cycles
:::

::: sol
**C6 (10 คะแนน)**

**(a)** Dependencies (3)

| คู่ | Register | ชนิด |
|---|---|---|
| 1 → 2 | r1 | RAW |
| 2 → 4 | r3 | RAW |
| 3 → 4 | r6 | RAW |

[**ไม่มี WAR/WAW**]{.ans} (ไม่มีคำสั่งใดเขียน register ซ้ำ หรือเขียนทับสิ่งที่คำสั่งก่อนหน้าอ่าน) ถ้าตอบว่ามีจะเสียคะแนน

**(b)** (3)
- 2 → 4 (r3) เป็นผล ALU จึง forward ได้ไม่ต้อง stall
- 1 → 2 และ 3 → 4 เป็น **load-use** → stall จุดละ 1 cycle
- ideal = 5 + 4 = 9 cycles → รวม [**11 cycles**]{.ans}

**(c)** (3)

```
1: LW   $r1, 0($r2)
3: LW   $r6, 4($r2)
2: ADD  $r3, $r1, $r4    ; ห่างจาก LW r1 สองคำสั่ง ใช้ forwarding ได้
5: ORI  $r8, $r9, #5     ; คำสั่งอิสระ คั่นระหว่าง LW r6 กับ SUB
4: SUB  $r7, $r6, $r3    ; r3 forward จาก ADD และ r6 พร้อมแล้ว
```

- → [**9 cycles ไม่มี stall**]{.ans} (speedup 11/9 = 1.22)
- ตรวจแล้วว่าไม่สร้าง WAR/WAW ใหม่ (ORI เขียน r8 ซึ่งไม่มีใครใช้)
- ลำดับอื่นที่ถูกก็ได้คะแนน เช่น LW, LW, ORI, ADD, SUB

**(d)** (1) [**Compiler scheduling / delayed load**]{.ans}: ย้ายคำสั่งอิสระมาคั่น ถ้าไม่มีให้แทรก **NOP** ให้ครบจำนวนที่ต้องรอ (สไลด์: `LW; NOP; NOP; NOP; AND`)
:::

::: sol
**C7 (6 คะแนน)**

**(a)** (2)
- offset = log₂4096 = [**12 bits**]{.ans}
- VPN = 32 − 12 = [**20 bits**]{.ans}
- PA = log₂(1 GB) = 30 bits → PPN = 30 − 12 = [**18 bits**]{.ans}

**(b)** 2²⁰ × 4 B = [**4 MB ต่อ process**]{.ans} (1)

**(c)** (2)
- overlap ได้เมื่อ **index + offset ≤ page offset (12 bits)** หรือก็คือ cache size / ways ≤ page size
- 32 KB / 4 KB = [**8-way**]{.ans} (แต่ละ way 4 KB ดังนั้นบิตที่ใช้ index ทั้งหมดอยู่ใน page offset ซึ่งไม่เปลี่ยนตอนแปล)
- ทางเลือกอื่น: page 32 KB หรือให้ OS รับประกันว่าบิต 14–12 ของ VA = PA (page coloring)

**(d)** (1)
- [**TLB: flush**]{.ans} (หรือใช้ ASID/PID tag) เพราะ mapping เป็นของ process เก่า
- **Page table: ไม่ต้องลบ** แค่เปลี่ยน page table register ให้ชี้ไปที่ table ของ process ใหม่
:::

::: sol
**C8 (เลือก 2 ข้อ ข้อละ 3 คะแนน)**

**(a) RAID 5 vs RAID 4**
- RAID 4 เก็บ parity บน**ดิสก์เฉพาะลูกเดียว** การเขียนทุกครั้งต้องอัปเดตดิสก์นั้น จึงเป็น **bottleneck**
- RAID 5 **กระจาย parity ไปทุกดิสก์** การเขียนหลาย stripe จึงทำขนานกันได้ (read ก็ใช้ได้ครบทุกดิสก์)
- ทั้งคู่ทนดิสก์เสียได้ 1 ลูก
- **RAID 0** เหมาะกับงานที่ต้องการ**ความเร็วสูงสุด**และข้อมูลไม่สำคัญหรือมี backup อยู่แล้ว (scratch, temp ของงานตัดต่อวิดีโอ) เพราะเสีย 1 ลูกข้อมูลหายหมด

**(b) Write-back vs Write-through**
- **Write-back:** เขียนเฉพาะ cache (ตั้ง dirty bit) แล้วค่อยเขียนกลับตอน replace → **เร็ว ดีกับการเขียนซ้ำ** แต่**ใน multiprocessor ข้อมูลจะ incoherent**
- **Write-through:** เขียนทั้งสองที่ทันที → **ช้า** แต่ memory เป็นปัจจุบันเสมอ **เหมาะกับ multiprocessor**
- **Write buffer:** FIFO ที่ทำให้ CPU ไม่ต้องรอ memory ตอน write-through
- **Saturate** เมื่ออัตราการเขียนสูงกว่าที่ memory รับไหว ซึ่งจะเต็มไม่ว่า buffer ใหญ่แค่ไหน → แก้ด้วย **L2 cache**

**(c) Row-major**
- **แบบ X เร็วกว่า** เพราะ C เก็บ array แบบ **row-major** (`data[r][0], data[r][1], …` อยู่ติดกัน) X จึงเดินเรียง address ทีละ 4 bytes ทำให้ได้ **spatial locality** (1 block มีหลาย element จึง hit ต่อเนื่อง)
- แบบ Y กระโดดทีละ 4000 bytes เกือบทุกครั้งตกคนละ block ทำให้ miss บ่อย และ block อาจถูกไล่ออกก่อนจะได้ใช้ element ถัดไป

**(d) Dynamic vs Static**
- **Dynamic:** HW ซับซ้อนและใช้ power มาก แต่ **binary เดิมรันได้และเร็วขึ้นบน HW ใหม่** (ไม่ต้อง recompile) และรู้ dependency จริงตอนรัน
- **Static (VLIW):** HW ง่ายและประหยัด power, compiler เห็น scope กว้าง แต่ **binary ผูกกับรุ่น HW** (Itanium → Itanium II ไม่ compatible) และ compiler รู้ dependency บางอย่างไม่ได้ (pointer alias, cache miss)
- **ในทางปฏิบัติ dynamic ชนะ** เพราะ compatibility และ "proven to be too difficult to have good compiler" (Itanium ถูก EOL ในปี 2019)
:::

## แปลผลคะแนนชุดที่ 2 (เต็ม 100)

| คะแนน | ระดับ | ทำต่อ |
|---|---|---|
| 85–100 | พร้อมมาก | ทบทวนกับดักรวม |
| 70–84 | พร้อม | ทำ Exercise ท้ายบทที่ผิดซ้ำ |
| 50–69 | ปานกลาง | อ่าน Ch2, Ch6, Ch8 ใน Exam Notes ใหม่ |
| < 50 | ต้องเร่ง | เริ่มจาก Formula Sheet แล้วไล่ตัวอย่างทุกบท |
