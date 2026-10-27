# Extra Practice Set (ข้อเขียนแบบยาว, Computer Architecture อย่างเดียว)

**เวลา 90 นาที · คะแนนเต็ม 100**
**ขอบเขต:** Chapter 1–9 (Introduction → Storage) ตามสไลด์ของ Krerk Piromsopa

| ส่วน | รูปแบบ | คะแนน | เวลาที่แนะนำ |
|---|---|---|---|
| A | เติมคำ (Fill in the blank) 20 ข้อ | 20 | 15 นาที |
| B | ปรนัย (Multiple choice) 20 ข้อ | 20 | 20 นาที |
| C | คำนวณและอธิบาย 8 ข้อ | 60 | 55 นาที |

> **กติกา:** ใช้เครื่องคิดเลขได้ ห้ามดูโน้ต และจับเวลาจริง เมื่อทำเสร็จค่อยตรวจกับ `05-extra-practice-answers.md`
> ข้อตกลงที่ใช้ทั้งฉบับ: 1 KB = 2¹⁰ bytes, address เป็น byte address และ 1 word = 4 bytes

---

## Part A: เติมคำ (ข้อละ 1 คะแนน, 20 คะแนน)

1. ISA เป็น abstraction/interface ระหว่าง ____________ กับ ____________
2. ในปี 1964 IBM ออกสถาปัตยกรรม ____________ ซึ่งรวม instruction set ที่ไม่เข้ากันได้ 7 แบบเข้าด้วยกัน
3. Core i3, i5 และ i7 ใช้ ISA เดียวกัน ความแตกต่างของมันจึงอยู่ที่ระดับ ____________
4. Benchmark ที่พยายามเลียนแบบพฤติกรรมของโปรแกรมจริง เช่น Whetstone และ Dhrystone เรียกว่า ____________ benchmark
5. เมื่อต้องสรุปผล benchmark ที่เป็น **ratio** (normalized speedup) ควรใช้ค่าเฉลี่ยแบบ ____________ mean
6. เก็บค่า `0xCAFE1234` แบบ **little endian** ที่ address 0x200 ไบต์ที่ address **0x201** คือ `0x____`
7. ภายใต้ restricted alignment ข้อมูลขนาด s ไบต์ต้องมี base address A ที่ทำให้ ____________ = 0
8. Addressing mode ของ `LD $r1, ($r2)+` ชื่อ ____________ ซึ่งตรงกับ C ว่า `A = D[____]`
9. ใน nanoLADA คำสั่ง I-type มี immediate ____ bits และ J-type มี address field ____ bits
10. คำสั่ง `ORUI` ใช้ extender แบบ ____________ ส่วน `LW`/`SW`/`BEQ` ใช้แบบ ____________
11. ใน single-cycle nanoLADA คำสั่งที่กำหนด critical path คือ ____________
12. ใน multi-cycle nanoLADA คำสั่ง LW, SW และ JMP ใช้ ____, ____ และ ____ cycles ตามลำดับ
13. Control unit ของ multi-cycle processor เป็น ____________ ซึ่งสร้างได้ด้วย sequential circuit หรือ ____________
14. ถ้า Wregs(i) ∩ Rregs(j) ≠ ∅ โดย j มาก่อน i จะเกิด data hazard ชนิด ____________
15. ตามหลัก Flynn's taxonomy, vector processor/GPU คือ ____________ และ multicore คือ ____________
16. Simultaneous Multithreading (SMT) ของ Intel มีชื่อทางการค้าว่า ____________
17. ____________ ใช้ capacitor ต้อง refresh และเหมาะเป็น main memory ส่วน ____________ ใช้ transistor และเหมาะเป็น cache
18. Miss ที่เกิดขึ้นทั้งที่ cache ยังมีที่ว่าง แต่ mapping บังคับให้ชนกัน เรียกว่า ____________ miss
19. Miss ใน virtual memory เรียกว่า ____________ และใช้นโยบายการเขียนแบบ write-____________ เท่านั้น
20. RAID ____ ใช้ parity สองชุดและทนดิสก์เสียได้ 2 ลูก ส่วน RAID 5 ต้องใช้ดิสก์อย่างน้อย ____ ลูก

---

## Part B: ปรนัย (ข้อละ 1 คะแนน, 20 คะแนน) เลือกคำตอบที่ถูกที่สุด

**B1.** ข้อใด**ไม่ใช่**สิ่งที่ ISA กำหนด
a) รูปแบบ (format) ของคำสั่ง  b) addressing modes  c) จำนวน cache level ใน CPU  d) วิธีจัดการ interrupt/exception

**B2.** Computer A มี 400 MIPS และรันโปรแกรมที่ compile ได้ 800 ล้านคำสั่ง ส่วน Computer B (ISA ต่างกัน) มี 300 MIPS และรันโปรแกรมเดียวกันที่ compile ได้ 500 ล้านคำสั่ง ข้อใดถูก
a) A เร็วกว่าเพราะ MIPS สูงกว่า  b) B เร็วกว่าประมาณ 1.2 เท่า  c) เร็วเท่ากัน  d) สรุปไม่ได้เพราะไม่รู้ clock rate

**B3.** สถาปัตยกรรมใดเหมาะกับ pipelining ที่สุด
a) Accumulator  b) Stack  c) Memory-Memory  d) Register-Register (Load-Store)

**B4.** ข้อใดเป็นข้อเสียของ Stack architecture ตามสไลด์
a) code density แย่  b) ข้อมูลที่ต้องการไม่ได้อยู่ top of stack เสมอ  c) ต้องใช้ hardware มาก  d) compiler เขียนยาก

**B5.** สำหรับการ**เปรียบเทียบ (มากกว่า/น้อยกว่า)** เลข 32 บิตบน bus 8 บิต endian แบบใดเร็วกว่า และเพราะอะไร
a) Little: ได้ byte ต่ำก่อน  b) Big: ได้ byte ที่มี sign bit ก่อน  c) Little: carry ถูกต้อง  d) เท่ากัน

**B6.** ระบบใช้ **Vector Table** ที่ base 0x8000 และ address ขนาด 4 bytes เมื่อเกิด interrupt หมายเลข 5 CPU จะอ่าน**ที่อยู่ของ handler** จาก address ใด
a) 0x8005  b) 0x8014  c) 0x8050  d) 0x8020

**B7.** วิธี clear register ที่สไลด์แนะนำสำหรับ architecture ส่วนใหญ่คือ
a) `CLR R1`  b) `MOV R1, 0`  c) `SUB R1,R1,R1`  d) `XOR R1,R1,R1`

**B8.** การย้าย `hs = 3600;` ที่เป็นค่าคงที่ออกไปไว้นอก loop เป็น optimization ประเภทใด
a) Strength reduction  b) Code motion  c) Procedure inlining  d) Pipeline scheduling

**B9.** ใน nanoLADA single-cycle คำสั่งใดมี `reg_wr = 0` และ `mem_wr = 1`
a) LW  b) SW  c) BEQ  d) ORI

**B10.** หลังรัน `ORUI $r1, $r0, #0xBEEF` ค่าของ $r1 คือ
a) 0x0000BEEF  b) 0xFFFFBEEF  c) 0xBEEF0000  d) 0xBEEFBEEF

**B11.** คำสั่ง `BEQ $r1, $r2, imm` อยู่ที่ PC = 0x0040 โดย imm = −3 และ R[r1] == R[r2] ค่า PC ถัดไปคือ
a) 0x0034  b) 0x0038  c) 0x003D  d) 0x0044

**B12.** Single-cycle มี cycle time 240 ns ส่วน multi-cycle มี cycle time 60 ns ถ้าต้องการให้ multi-cycle เร็ว**อย่างน้อยเท่ากับ** single-cycle ค่า average CPI ต้องเป็นเท่าไร
a) ≥ 4  b) ≤ 4  c) ≤ 5  d) = 1

**B13.** ข้อใด**ถูก**เกี่ยวกับ pipelining
a) ลด latency ของแต่ละคำสั่ง  b) เพิ่ม throughput โดย clock ถูกจำกัดด้วย stage ที่ช้าที่สุด  c) speedup เท่ากับจำนวน stage พอดีเสมอ  d) stage ไม่สมดุลไม่มีผล

**B14.** การแยก instruction cache กับ data cache ช่วยแก้ hazard ชนิดใด
a) Structural  b) Data (RAW)  c) Control  d) WAW

**B15.** ใน 5-stage pipeline ที่มี forwarding ครบ ลำดับคำสั่งใดที่**ยังต้อง stall**
a) `ADD r1,..` ตามด้วย `SUB ..,r1,..`  b) `LW r1,0(r2)` ตามด้วย `ADD r3,r1,r4`  c) `SW r1,0(r2)` ตามด้วย `ADD r3,r4,r5`  d) `ADD r1,..` ตามด้วย `SW r1,0(r2)`

**B16.** ข้อใดอธิบาย **branch delay slot** ได้ถูกต้อง
a) hardware ยกเลิกคำสั่งหลัง branch ทุกครั้ง  b) คำสั่งที่อยู่ถัดจาก branch จะถูก execute เสมอ ไม่ว่า branch จะ taken หรือไม่  c) เป็นวิธีทาย branch ด้วย history  d) ไม่ต้องอาศัย compiler

**B17.** Superscalar degree 2 กับ pipeline 5 stage รัน 1000 คำสั่ง (ideal) ใช้เวลาประมาณกี่ T_c
a) 1004  b) 504  c) 502  d) 1000

**B18.** ข้อใด**ถูก**เกี่ยวกับ VLIW
a) ใช้ dynamic scheduling ใน hardware  b) ลด CPI แต่ไม่ลด IC  c) ใช้ static scheduling ทำให้ binary ข้ามรุ่น (เช่น Itanium → Itanium II) ไม่ compatible  d) Intel Itanium ยังผลิตอยู่และได้รับความนิยม

**B19.** การเพิ่ม associativity จาก direct-mapped เป็น 4-way (cache size เท่าเดิม) มีผลข้อใดมากที่สุด
a) ลด compulsory miss  b) ลด conflict miss แต่ hit time อาจเพิ่มขึ้น  c) ลด capacity miss เป็นศูนย์  d) ทำให้ไม่ต้องมี tag

**B20.** Amazon EBS และ NAS ที่ใช้ NFS ให้บริการ storage ระดับใดตามลำดับ
a) Block, File  b) File, Block  c) Object, File  d) Block, Object

---

## Part C: คำนวณและอธิบาย (60 คะแนน) แสดงวิธีทำ

### C1. CPU Performance (8 คะแนน)
โปรแกรมหนึ่งมี 10⁹ คำสั่ง รันบน CPU 2.5 GHz โดยมี instruction mix ดังนี้

| Class | สัดส่วน | CPI |
|---|---|---|
| ALU | 50% | 1 |
| Load | 20% | 5 |
| Store | 10% | 4 |
| Branch | 20% | 3 |

(a) หา average CPI และ CPU time (3 คะแนน)
(b) ถ้าปรับปรุง memory จน CPI ของ Load ลดเหลือ 3 จะได้ speedup เท่าไร (2 คะแนน)
(c) แสดงว่าคำตอบข้อ (b) ได้ค่าเท่ากันเมื่อใช้ **Amdahl's Law** และอธิบายว่า P ที่ต้องใช้คืออะไร ทำไม**ไม่ใช่** 20% (3 คะแนน)

### C2. Amdahl's Law (5 คะแนน)
โปรแกรมหนึ่งใช้เวลา 70% กับส่วนที่ทำ parallel ได้
(a) ถ้ารันบน 8 cores จะได้ overall speedup เท่าไร (2 คะแนน)
(b) speedup สูงสุดที่เป็นไปได้ (cores → ∞) คือเท่าไร (1 คะแนน)
(c) ทีมงานมีสองทางเลือก คือ (i) เพิ่ม cores จาก 8 เป็น 64 หรือ (ii) ทำให้ส่วน serial เร็วขึ้น 2 เท่า (ยังคง 8 cores) ทางไหนดีกว่า แสดงตัวเลข (2 คะแนน)

### C3. Single-cycle vs Multi-cycle vs Pipeline: nanoLADA (9 คะแนน)
พิจารณาโปรแกรมต่อไปนี้ (BEQ **not taken**)
```
LW   $r1, 0($r10)
LW   $r2, 4($r10)
ADD  $r3, $r1, $r2
ORI  $r4, $r3, #1
SW   $r4, 8($r10)
BEQ  $r1, $r2, SKIP
JMP  END
```
กำหนดให้ single-cycle มี cycle time = 230 ns, multi-cycle มี cycle time = 50 ns และ pipeline 5 stage มี cycle time = 50 ns (ideal ไม่มี stall)
(a) หาเวลาที่ใช้บน single-cycle (2 คะแนน)
(b) หาจำนวน cycle และเวลาที่ใช้บน multi-cycle (3 คะแนน)
(c) หาเวลาที่ใช้บน ideal pipeline และ speedup เทียบกับ single-cycle (2 คะแนน)
(d) ในความเป็นจริง pipeline นี้จะเจอ hazard อย่างน้อย 2 จุด ให้ระบุว่าอยู่ระหว่างคำสั่งใดและเป็นชนิดใด (2 คะแนน)

### C4. Cache Address Mapping (10 คะแนน)
ระบบมี address 32 bit และ **direct-mapped cache ขนาด 16 KB** โดย **block size 32 bytes**
(a) หาจำนวนบิตของ tag, index และ offset (3 คะแนน)
(b) หา tag, index และ offset (เลขฐานสิบ) ของ address `0x00012345` (3 คะแนน)
(c) address `0x00016345` จะ hit หรือ conflict กับ `0x00012345` หรือไม่ อธิบาย (2 คะแนน)
(d) ถ้าเปลี่ยนเป็น **2-way set associative** ขนาดเท่าเดิม จำนวนบิตของ tag/index/offset จะเป็นเท่าไร และต้องใช้ comparator กี่ตัว (2 คะแนน)

### C5. Cache Performance (6 คะแนน)
(a) CPU มี CPI_ideal = 1 และ 30% ของคำสั่งเป็น load/store โดย instruction-cache miss rate = 2%, data-cache miss rate = 5% และ miss penalty = 100 cycles จงหา CPI จริง และบอกว่าช้ากว่า CPU ที่มี cache สมบูรณ์แบบกี่เท่า (3 คะแนน)
(b) ระบบ 2-level มี L1 hit time 1 cycle, L1 miss rate 5%, L2 hit time 10 cycles, L2 (local) miss rate 20% และ memory 100 cycles จงหา AMAT (3 คะแนน)

### C6. Pipeline Hazards & Scheduling (10 คะแนน)
พิจารณา 5-stage pipeline (IF, ID, EX, MEM, WB) ที่มี **full forwarding** โดย register file เขียนครึ่งแรกของ cycle และอ่านครึ่งหลัง
```
1: LW   $r1, 0($r2)
2: ADD  $r3, $r1, $r4
3: LW   $r6, 4($r2)
4: SUB  $r7, $r6, $r3
5: ORI  $r8, $r9, #5
```
(a) ระบุ data dependency ทั้งหมด (คู่คำสั่ง, register และชนิด RAW/WAR/WAW) (3 คะแนน)
(b) dependency ใดบ้างที่ forwarding แก้ได้โดยไม่ต้อง stall และจุดใดที่ยังต้อง stall รวมแล้วโปรแกรมนี้ใช้กี่ cycle (3 คะแนน)
(c) **Reschedule** โปรแกรมให้ไม่มี stall เลย (ผลลัพธ์ต้องถูกต้องเหมือนเดิม) และบอกจำนวน cycle ใหม่ (3 คะแนน)
(d) ถ้าโปรแกรมนี้รันบน machine ที่**ไม่มี forwarding เลย** (ต้องรอ WB) วิธีที่ software ใช้แก้ hazard ที่เหลือโดยไม่ต้องให้ hardware detect คืออะไร (1 คะแนน)

### C7. Virtual Memory & TLB (6 คะแนน)
ระบบมี virtual address 32 bit, page size 4 KB, physical memory 1 GB และ page table entry ขนาด 4 bytes
(a) หาจำนวนบิตของ VPN, page offset และ PPN (2 คะแนน)
(b) page table ของแต่ละ process มีขนาดเท่าไร (1 คะแนน)
(c) สถาปนิกต้องการ **L1 cache ขนาด 32 KB** ที่ทำ **overlapped cache & TLB access** ได้ cache ต้องมี associativity อย่างน้อยเท่าไร อธิบาย (2 คะแนน)
(d) เมื่อ OS ทำ process switch ต้องทำอะไรกับ TLB และ page table (1 คะแนน)

### C8. อธิบายสั้น ๆ (6 คะแนน) **เลือกตอบ 2 ข้อจาก 4 ข้อ** (ข้อละ 3 คะแนน)
(a) ทำไม **RAID 5** จึงเขียนได้เร็วกว่า **RAID 4** และ RAID 0 เหมาะกับงานแบบใด
(b) เปรียบเทียบ **write-back** กับ **write-through** ในแง่ความเร็วและการใช้งานกับ multiprocessor และอธิบายว่า write buffer มีไว้ทำอะไร และเมื่อไรที่มันจะ saturate
(c) โค้ดสองแบบนี้ให้ผลลัพธ์เหมือนกัน แบบไหนเร็วกว่าเพราะอะไร
```c
int data[1000][1000];
// แบบ X                                   // แบบ Y
for (r=0;r<1000;r++)                      for (c=0;c<1000;c++)
  for (c=0;c<1000;c++) sum+=data[r][c];     for (r=0;r<1000;r++) sum+=data[r][c];
```
(d) เปรียบเทียบ **dynamic scheduling** (superscalar out-of-order) กับ **static scheduling** (VLIW) ในแง่ hardware, compatibility และ performance ของ legacy software แล้วบอกว่าในทางปฏิบัติฝั่งไหน "ชนะ" เพราะอะไร

---
*จบข้อสอบ ตรวจคำตอบกับ `05-extra-practice-answers.md`*
