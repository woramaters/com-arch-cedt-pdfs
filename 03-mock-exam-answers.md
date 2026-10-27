# เฉลย Mock Exam: Computer Architecture

> ให้คะแนนตัวเองตามที่ระบุไว้แต่ละข้อ ข้อเขียนได้คะแนนเต็มเมื่อ **มีทั้งหลักการ เหตุผล และตัวเลขหรือตัวอย่าง** ประกอบ

---

## Part A: เติมคำ

| # | คำตอบ | หมายเหตุ |
|---|---|---|
| 1 | **software, hardware** | |
| 2 | **IBM 360** (System/360) | ก่อนหน้านี้โปรแกรมไม่ portable |
| 3 | **Organization** (computer organization / microarchitecture) | ต่างกันที่จำนวน core, cache, Turbo Boost, Hyper-Threading |
| 4 | **Synthetic** | |
| 5 | **Geometric** | |
| 6 | **0x12** | 0x200=34, **0x201=12**, 0x202=FE, 0x203=CA |
| 7 | **A mod s** | |
| 8 | **Auto-increment**, `D[i++]` | |
| 9 | **16**, **26** | |
| 10 | **Zero pad** (imm ไปอยู่ 16 บิตบน), **Sign extend** | ORI ใช้ zero extend |
| 11 | **LW** | 10+40+40+20+10+60+40+10 = 230 ns |
| 12 | **5, 4, 3** | |
| 13 | **Finite State Machine (FSM)**, **Microprogram** (microcode / ROM) | |
| 14 | **WAR** (Write After Read) | i เขียนสิ่งที่ j อ่าน |
| 15 | **SIMD**, **MIMD** | |
| 16 | **Hyper-Threading** | |
| 17 | **DRAM**, **SRAM** | |
| 18 | **Conflict** | |
| 19 | **Page fault**, write-**back** | |
| 20 | **6**, **3** | |

---

## Part B: ปรนัย

| # | ตอบ | เหตุผล |
|---|---|---|
| B1 | **c** | จำนวน cache level เป็นเรื่องของ **organization** ซึ่ง software มองไม่เห็นผ่าน ISA |
| B2 | **b** | T_A = 8×10⁸ / 4×10⁸ = 2 s และ T_B = 5×10⁸ / 3×10⁸ = 1.67 s → B เร็วกว่า 2/1.67 = **1.2 เท่า** (ไม่ต้องรู้ clock เพราะ MIPS รวมไว้แล้ว) → **MIPS สูงกว่าไม่ได้แปลว่าเร็วกว่า** |
| B3 | **d** | Load-store มี fixed-length format และ CPI ใกล้เคียงกัน จึงทำ pipeline ได้ง่าย |
| B4 | **b** | Stack มี code density ดีและ compiler เขียนง่าย แต่ข้อมูลไม่ได้อยู่ top เสมอ และ stack เป็น bottleneck |
| B5 | **b** | big endian ให้ byte สูง (มี sign bit) มาก่อน จึงตอบได้ทันที ส่วน little endian ดีกับ**การบวก** |
| B6 | **b** | 0x8000 + 5 × 4 = 0x8000 + 20 = 0x8000 + 0x14 = **0x8014** (ถ้าเป็น Handler Table ขนาด 16 bytes จะได้ 0x8050 ซึ่งเป็นตัวลวง) |
| B7 | **d** | XOR R1,R1,R1 ไม่ต้องใช้ immediate encode สั้น และ HW ส่วนใหญ่รู้จัก idiom นี้ |
| B8 | **b** | Code motion (ย้าย loop-invariant ออกนอก loop) เป็น global optimization |
| B9 | **b** | SW: reg_wr=0, mem_wr=1 |
| B10 | **c** | zero_pad → imm อยู่ 16 บิตบน แล้ว OR กับ $r0 = 0 ได้ 0xBEEF0000 |
| B11 | **b** | PC+4 = 0x44 แล้วบวก (−3 × 4) = −12 = −0xC ได้ **0x38** |
| B12 | **b** | CPI × 60 ≤ 240 → **CPI ≤ 4** |
| B13 | **b** | |
| B14 | **a** | memory เดียวกันถูกใช้พร้อมกันทั้ง IF และ MEM เป็น structural hazard ซึ่งแก้ด้วยการแยก I/D cache |
| B15 | **b** | load-use: ข้อมูลพร้อมตอนจบ MEM แต่ ADD ต้องใช้ตอนต้น EX ใน cycle เดียวกัน จึงต้อง stall 1 cycle ("ต้องมีไทม์แมชชีน") |
| B16 | **b** | ต้องให้ compiler หาคำสั่งอิสระมาใส่ ถ้าไม่มีให้ใส่ NOP |
| B17 | **b** | T = (k + (n−x)/x) T_c = 5 + 998/2 = 5 + 499 = **504 T_c** (ตัวเลือก a คือ pipeline ธรรมดา) |
| B18 | **c** | VLIW ใช้ static scheduling ซึ่ง**ลด IC** (หลาย op ต่อ word) Intel ประกาศ EOL ของ Itanium ในปี 2019 |
| B19 | **b** | associativity ลด conflict miss แต่ต้องมี comparator/MUX มากขึ้น hit time จึงอาจเพิ่ม |
| B20 | **a** | EBS = block และ NFS = file (NAS) |

---

## Part C: คำนวณและอธิบาย

### C1 (8 คะแนน)
**(a)**
CPI_avg = 0.5(1) + 0.2(5) + 0.1(4) + 0.2(3) = 0.5 + 1.0 + 0.4 + 0.6 = **2.5** ✔(1.5)

CPU time = IC × CPI / f = 10⁹ × 2.5 / (2.5 × 10⁹) = **1.0 s** ✔(1.5)

**(b)**
CPI_ใหม่ = 0.5 + 0.2(3) + 0.4 + 0.6 = **2.1**

Speedup = 2.5 / 2.1 = **1.19** ✔(2) (IC และ clock เท่าเดิมจึงตัดทิ้งได้)

**(c)** Amdahl ต้องใช้ **P = สัดส่วนของ "เวลา"** ที่ใช้กับ load ไม่ใช่สัดส่วนของ "จำนวนคำสั่ง" ✔(1)
- เวลาของ load คิดเป็น 1.0/2.5 = **P = 0.4** (40%) ✔(1)
- ส่วนนั้นเร็วขึ้น n = 5/3 เท่า
- Speedup = 1 / (0.6 + 0.4/(5/3)) = 1 / (0.6 + 0.24) = 1/0.84 = **1.19** ✔(1), ตรงกับข้อ (b)

ถ้าแทน P = 0.2 จะได้ 1/(0.8 + 0.12) = 1.087 ซึ่ง**ผิด** เพราะ load แต่ละคำสั่งใช้เวลามากกว่าคำสั่งเฉลี่ย

### C2 (5 คะแนน)
**(a)** S = 1 / (0.3 + 0.7/8) = 1/0.3875 = **2.58** ✔(2)

**(b)** S_max = 1/0.3 = **3.33** ✔(1)

**(c)** ✔(2)
- (i) 64 cores: 1/(0.3 + 0.7/64) = 1/0.3109 = **3.22**
- (ii) serial เร็วขึ้น 2 เท่า + 8 cores: 1/(0.15 + 0.0875) = 1/0.2375 = **4.21**
- → **(ii) ดีกว่า** เพราะส่วน serial เป็นตัวจำกัด speedup (Amdahl, "make the common case fast") การเพิ่ม core ให้ผลแบบ diminishing returns

### C3 (9 คะแนน)
**(a)** Single-cycle มี CPI = 1: 7 × 230 = **1610 ns** ✔(2)

**(b)** Multi-cycle ✔(3):

| Instr | LW | LW | ADD | ORI | SW | BEQ | JMP | รวม |
|---|---|---|---|---|---|---|---|---|
| Cycles | 5 | 5 | 4 | 4 | 4 | 3 | 3 | **28** |

28 × 50 = **1400 ns** (CPI เฉลี่ย = 4.0 → เร็วกว่า single-cycle เพียง 1610/1400 = 1.15 เท่า)

**(c)** Pipeline: (k + n − 1) × T_c = (5 + 7 − 1) × 50 = 11 × 50 = **550 ns** ✔(1)

Speedup เทียบ single-cycle = 1610/550 = **2.93** ✔(1) (ไม่ถึง 5 เพราะ n น้อย เวลา fill จึงมีผลมาก และ 5 × 50 = 250 > 230)

**(d)** ตอบอย่างน้อย 2 ข้อ ✔(2):
- **RAW (load-use)** บน **$r2**: `LW $r2` → `ADD $r3,$r1,$r2` (และ $r1 จาก LW แรกก็เป็น RAW ด้วย แต่ห่างกัน 2 คำสั่ง forwarding จึงแก้ได้)
- **RAW** บน **$r3**: `ADD` → `ORI`
- **RAW** บน **$r4**: `ORI` → `SW`
- **Control hazard**: `BEQ` (และ `JMP`) เพราะยังไม่รู้ว่าคำสั่งถัดไปคืออะไรจนกว่า branch จะ resolve

### C4 (10 คะแนน)
**(a)** ✔(3)
- Offset = log₂32 = **5 bits**
- จำนวน lines = 16 KB / 32 B = 512 → index = **9 bits**
- Tag = 32 − 9 − 5 = **18 bits**

**(b)** 0x00012345 = 74,565 (ฐานสิบ) ✔(3)
- **Offset** = 74,565 mod 32 = **5**
- **Index** = (74,565 mod 16,384) div 32 = 9,029 div 32 = **282**
- **Tag** = 74,565 div 16,384 = **4**

ตรวจด้วย binary: 0x12345 = `0001 0010 0011 0100 0101`
- 5 บิตล่าง = 00101 = 5
- 9 บิตถัดมา = 1 0001 1010 = 0x11A = 282
- ที่เหลือ = 0100 = 4

**(c)** 0x00016345 = 0x12345 + 0x4000 (+16,384 = ขนาด cache พอดี) ✔(2)
- index = **282** และ offset = **5** เหมือนเดิม แต่ tag = 90,949 div 16,384 = **5 ≠ 4**
- → ตกที่ line เดียวกันแต่ tag ต่างกัน = **conflict miss** สองตัวนี้จะไล่กันออกไปมา (ping-pong ถ้าใช้สลับกัน)

**(d)** 2-way: จำนวน sets = 512/2 = 256 ✔(2)
- **Offset 5, index 8, tag 19 bits**
- ใช้ **2 comparators** (หนึ่งตัวต่อ way)
- ทั้งสอง address อยู่ set 282 mod 256 = 26 ได้พร้อมกัน → conflict หายไป

### C5 (6 คะแนน)
**(a)** ✔(3)
- ทุกคำสั่งต้อง fetch (1 access) และ 30% มี data access เพิ่ม
- CPI = 1 + (1 × 0.02 × 100) + (0.3 × 0.05 × 100) = 1 + 2 + 1.5 = **4.5**
- ช้ากว่า perfect cache **4.5 เท่า** → memory stall คิดเป็น 3.5/4.5 ≈ 78% ของเวลา

**(b)** ✔(3)
- Miss penalty ของ L1 = AMAT ของ L2 = 10 + 0.2 × 100 = 30 cycles
- AMAT = 1 + 0.05 × 30 = **2.5 cycles**
- (ถ้าไม่มี L2: 1 + 0.05 × 100 = 6 cycles → L2 ช่วยลด miss penalty ได้มาก)

### C6 (10 คะแนน)
**(a)** Dependencies ✔(3):

| คู่ | Register | ชนิด |
|---|---|---|
| 1 → 2 | $r1 | RAW |
| 2 → 4 | $r3 | RAW |
| 3 → 4 | $r6 | RAW |

**ไม่มี WAR/WAW** (ไม่มีคำสั่งไหนเขียน register ซ้ำ หรือเขียนทับสิ่งที่คำสั่งก่อนหน้าอ่าน) ถ้าตอบว่ามี WAR/WAW จะเสียคะแนน

**(b)** ✔(3)
- 2 → 4 ($r3): ADD เป็น ALU op จึง **forward ได้โดยไม่ stall**
- 1 → 2 และ 3 → 4 เป็น **load-use** → **stall จุดละ 1 cycle**
- Ideal = 5 + (5 − 1) = 9 cycles → รวม 9 + 2 = **11 cycles**

**(c)** Reschedule ✔(3):
```
1: LW   $r1, 0($r2)
3: LW   $r6, 4($r2)
2: ADD  $r3, $r1, $r4     ← ห่างจาก LW $r1 2 คำสั่ง ใช้ forwarding ได้
5: ORI  $r8, $r9, #5      ← คำสั่งอิสระ คั่นระหว่าง LW $r6 กับ SUB
4: SUB  $r7, $r6, $r3     ← $r3 forward จาก ADD และ $r6 พร้อมแล้ว
```
→ **9 cycles, ไม่มี stall** (speedup 11/9 = 1.22)
- ตรวจแล้วว่าการย้ายไม่สร้าง WAR/WAW ใหม่ เพราะ ORI เขียน $r8 ซึ่งไม่มีใครใช้
- ลำดับอื่นที่ถูกก็ได้คะแนน เช่น `LW r1; LW r6; ORI; ADD; SUB`

**(d)** ✔(1) **Compiler scheduling / delayed load:** ย้ายคำสั่งอิสระมาคั่น ถ้าไม่มีให้แทรก **NOP** ให้ครบจำนวนที่ต้องรอ (ตัวอย่างในสไลด์ `LW; NOP; NOP; NOP; AND`) ซึ่งเป็นความรับผิดชอบของ software ทั้งหมด

### C7 (6 คะแนน)
**(a)** ✔(2)
- Page offset = log₂4096 = **12 bits**
- VPN = 32 − 12 = **20 bits**
- Physical address = log₂(1 GB) = 30 bits → PPN = 30 − 12 = **18 bits**

**(b)** 2²⁰ × 4 B = **4 MB ต่อ process** ✔(1)

**(c)** ✔(2) Overlapped access ทำได้เมื่อ **index + offset ของ cache ไม่เกิน page offset (12 bits)** ซึ่งเทียบเท่ากับ **cache size / ways ≤ page size**
- 32 KB / 4 KB = **8 → ต้องเป็น 8-way set associative อย่างน้อย**
- แต่ละ way มี 4 KB ดังนั้น bits ที่ใช้ index ทั้งหมดมาจาก page offset ซึ่งไม่เปลี่ยนตอนแปล address → เปิด cache กับ TLB พร้อมกันได้
- ทางเลือกอื่น: ใช้ page 32 KB หรือให้ OS รับประกันว่า VA bits [14:12] = PA bits [14:12] (page coloring)

**(d)** ✔(1)
- **TLB:** flush (หรือใช้ ASID/PID tag) เพราะ mapping เป็นของ process เก่า
- **Page table:** ไม่ต้องลบ (มีต่อ process) แค่เปลี่ยน **page table register** ให้ชี้ไปที่ table ของ process ใหม่

### C8 (เลือก 2 ข้อ ข้อละ 3 คะแนน)
**(a) RAID 5 vs RAID 4**
- RAID 4 เก็บ parity บน**ดิสก์เฉพาะลูกเดียว** การเขียนทุกครั้งต้องอัปเดต parity ที่ดิสก์ลูกนั้น จึงเป็น **bottleneck** (write หลายครั้งทำขนานกันไม่ได้)
- RAID 5 **กระจาย parity ไปทุกดิสก์** การเขียนที่ไปคนละ stripe จึงอัปเดต parity คนละดิสก์พร้อมกันได้ (read ก็ใช้ได้ครบทุกดิสก์)
- ทั้งคู่ทนดิสก์เสียได้ 1 ลูก
- **RAID 0** (stripe) เหมาะกับงานที่ต้องการ **ความเร็วสูงสุดและข้อมูลไม่สำคัญ / มี backup** (เช่น scratch, cache, video editing temp) เพราะไม่มี redundancy เสีย 1 ลูกข้อมูลหายหมด

**(b) Write-back vs Write-through**
- **Write-back:** เขียนลง cache อย่างเดียว (ตั้ง dirty bit) แล้วเขียนกลับตอน replace → **เร็ว และดีกับ repeated write** แต่ใน **multiprocessor ข้อมูลใน memory/cache อื่นจะ incoherent**
- **Write-through:** เขียนทั้ง cache และ memory → **ช้าและแย่กับ repeated write** แต่ memory เป็นปัจจุบันเสมอ จึง **เหมาะกับ multiprocessor**
- **Write buffer:** FIFO เล็ก ๆ ที่ทำให้ CPU ไม่ต้องรอ memory ตอน write-through (มีคนวิ่งไปส่งให้แทน)
- **Saturate** เมื่ออัตราการเขียนสูงกว่าที่ memory รับไหว ซึ่งจะเต็มไม่ว่า buffer ใหญ่แค่ไหน → แก้ด้วยการเพิ่ม **L2 cache**

**(c) Row-major**
- **แบบ X เร็วกว่า** เพราะ C เก็บ 2D array แบบ **row-major** (`data[r][0], data[r][1], …` อยู่ติดกัน)
- แบบ X เดินตาม memory ทีละ 4 bytes จึงได้ **spatial locality**: block เดียวมีหลาย element ทำให้ hit ต่อเนื่อง
- แบบ Y กระโดดทีละ 1000 × 4 = 4000 bytes ทุกครั้ง เกือบทุก access จึงอยู่คนละ block → miss บ่อย และ block ที่โหลดมาอาจถูกไล่ออกก่อนจะได้ใช้ element ถัดไป

**(d) Dynamic vs Static scheduling**

| | Dynamic (superscalar OoO) | Static (VLIW) |
|---|---|---|
| Hardware | ซับซ้อน ใช้ power สูง | ง่าย ใช้ power ต่ำ |
| Compatibility | binary เดิมรันได้ | binary ผูกกับ HW รุ่นนั้น (Itanium → Itanium II ไม่ compatible) |
| Legacy software | **เร็วขึ้นบน HW ใหม่โดยไม่ต้อง recompile** | ต้อง recompile |
| ข้อจำกัด | | compiler รู้ dependency บางอย่างตอน compile ไม่ได้ (alias, cache miss) |

- ข้อดีของ static: compiler เห็น scope กว้างกว่า
- **ในทางปฏิบัติ dynamic ชนะ** เพราะ compatibility และ "proven to be too difficult to have good compiler" (Itanium ถูก EOL ในปี 2019)

---

## ตารางแปลผลคะแนน

| คะแนน | ความพร้อม | ควรทำต่อ |
|---|---|---|
| 85–100 | พร้อมมาก | ทบทวน "กับดัก" ท้าย `01-exam-notes.md` |
| 70–84 | พร้อม | ทำ Exercise ท้ายสไลด์แต่ละบทซ้ำในส่วนที่ผิด |
| 50–69 | ปานกลาง | อ่าน Ch2, Ch6 และ Ch8 ใน notes ใหม่ แล้วทำ Part C อีกรอบ |
| < 50 | ต้องเร่ง | เริ่มจากสูตรใน Formula Sheet แล้วทำตัวอย่างในสไลด์ทุกข้อ |
