# เฉลยละเอียด ชุดที่ 4

## ตารางคำตอบ (ตรวจเร็ว)

| ข้อ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ตอบ | a | b | a | b | d | b | a | b | c | c |
| **ข้อ** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** |
| ตอบ | b | b | c | c | b | c | a | a | a | d |
| **ข้อ** | **21** | **22** | **23** | **24** | **25** | **26** | **27** | **28** | **29** | **30** |
| ตอบ | a | d | b | c | d | a | c | b | d | c |
| **ข้อ** | **31** | **32** | **33** | **34** | **35** | **36** | **37** | **38** | **39** | **40** |
| ตอบ | a | b | c | a | d | b | a | b | a | c |

**แยกคะแนน:** Digital Logic = ข้อ 1–11 + S1–S2 (เต็ม 15) · Computer Architecture = ข้อ 12–40 + S3–S10 (เต็ม 45)

**ข้อไหนอยู่บทไหน:**

| บท | ข้อ |
|---|---|
| Digital Logic | 1–11, S1, S2 |
| Ch1 Introduction | 12 |
| Ch2 Performance | 14–19, S3, S4 |
| Ch3 ISA | 20–25, S5 |
| Ch4 Single cycle | 26, 27 |
| Ch5 Multi cycle | 28, 29, S6 |
| Ch6 Pipelining | 13, 30–33, S7 |
| Ch7 ILP | 34, 35 |
| Ch8 Memory | 36–39, S8, S9 |
| Ch9 Storage | 40, S10 |

## Part 1: Choice

### Digital Logic

::: sol
**1. ตอบ [a) 0xD6]{.ans}**

แบ่งทีละ 4 บิต: 1101 = D และ 0110 = 6 → **0xD6** (ตัวลวง b สลับลำดับ nibble)
:::

::: sol
**2. ตอบ [b) 229]{.ans}**

3 × 64 + 4 × 8 + 5 = 192 + 32 + 5 = **229**
:::

::: sol
**3. ตอบ [a) 0 ถึง 1023]{.ans}**

Unsigned n bits: 0 ถึง 2ⁿ − 1 = 2¹⁰ − 1 = 1023

- **ตัวลวง c:** ลืมลบ 1
- **ตัวลวง b:** เป็นช่วงของ 2's complement
:::

::: sol
**4. ตอบ [b) 1010 0101]{.ans}**

+90 = 0101 1010 → 1's complement = **กลับทุกบิต** = 1010 0101

- **ตัวลวง a (1010 0110):** เป็น **2's complement** (กลับบิตแล้วบวก 1)
- **ตัวลวง d:** เป็น +90
:::

::: sol
**5. ตอบ [d) carry out = 1, overflow = 1]{.ans}**

1001 0000 + 1010 0000 = **1** 0011 0000
- **carry out = 1**
- ผลคือ 0x30 = +48 ซึ่งเป็น **ลบ + ลบ ได้บวก** → **overflow = 1** ((−112) + (−96) = −208 ต่ำกว่า −128)
:::

::: sol
**6. ตอบ [b) A'B + AB']{.ans}**

XOR เป็น 1 เมื่ออินพุต**ต่างกัน** → แถว 01 (A'B) และ 10 (AB')

- **ตัวลวง a:** เป็น **XNOR** (เท่ากัน)
:::

::: sol
**7. ตอบ [a) AB + A'C]{.ans}**

**Consensus theorem:** พจน์ BC เป็น consensus ของ AB กับ A'C จึงตัดทิ้งได้

ตรวจ: ถ้า B = C = 1 แล้ว A = 1 ทำให้ AB = 1 และ A = 0 ทำให้ A'C = 1 → BC ถูกครอบคลุมเสมอ
:::

::: sol
**8. ตอบ [b) C']{.ans}**

m0, 2, 4, 6 = 000, 010, 100, 110 → **C = 0 ทุกตัว** → F = C'
:::

::: sol
**9. ตอบ [c) 7]{.ans}**

ต่อเป็นต้นไม้ 3 ชั้น: 4 + 2 + 1 = **7** ตัว (8 อินพุตลดลงทีละครึ่งจนเหลือ 1)

- **ตัวลวง a (3):** เป็นจำนวน select lines
:::

::: sol
**10. ตอบ [c) D flip-flop]{.ans}**

**Flip-flop = edge-triggered** ส่วน **latch = level-sensitive** (โปร่งใสตลอดช่วงที่ enable) และ combinational circuit ไม่มีหน่วยความจำเลย
:::

::: sol
**11. ตอบ [b) 3]{.ans}**

Mealy ไม่ต้องมี state "เห็นครบ 101" เพราะ output อยู่บนเส้น transition
- S0 = เริ่มต้น, S1 = เห็น "1", S2 = เห็น "10"
- จาก S2 ได้ 1 → output 1 แล้วไป S1 (overlapping)

(Moore ต้องใช้ 4 states ซึ่งเป็นตัวลวง c)
:::

### Computer Architecture

::: sol
**12. ตอบ [b) ISA]{.ans}**

ลำดับชั้นในสไลด์: Application → OS/Compiler → **ISA** → Firmware → Processor/I/O → Datapath & Control → Digital design → Circuit → Layout

ISA คือ interface ระหว่าง software กับ hardware
:::

::: sol
**13. ตอบ [c) Throughput]{.ans}**

Lessons learned: "Pipelining doesn't help **latency** of single task, it helps **throughput** of entire workload"
:::

::: sol
**14. ตอบ [c) Elapsed (wall-clock) time]{.ans}**

- **real** = เวลาจริงที่ผ่านไป
- **user** = CPU time ใน user mode
- **sys** = CPU time ใน kernel
:::

::: sol
**15. ตอบ [b) 1.5]{.ans}**

T<sub>X</sub> / T<sub>Y</sub> = 30/20 = **1.5**

- **ตัวลวง a (0.67):** เป็น "X เร็วกว่า Y กี่เท่า" (คือช้ากว่า)
:::

::: sol
**16. ตอบ [c) 2 s]{.ans}**

CPU time = cycles / f = 3 × 10⁹ / 1.5 × 10⁹ = **2 s**

- **ตัวลวง d (4.5 s):** คูณแทนหาร
:::

::: sol
**17. ตอบ [a) 1.7]{.ans}**

0.6(1) + 0.3(2) + 0.1(5) = 0.6 + 0.6 + 0.5 = **1.7**

- **ตัวลวง b (2.67):** เฉลี่ย 1, 2, 5 แบบไม่ถ่วงน้ำหนัก
:::

::: sol
**18. ตอบ [a) 1.33]{.ans}**

1 / (0.5 + 0.5/2) = 1/0.75 = **1.33**

- **ตัวลวง c (2):** คิดว่าทั้งโปรแกรมเร็วขึ้นเท่าส่วนที่เร่ง
:::

::: sol
**19. ตอบ [a) 4]{.ans}**

GM = √(2 × 8) = √16 = **4**

- **ตัวลวง b (5):** เป็น arithmetic mean
- **ตัวลวง d (3.2):** เป็น harmonic mean
:::

::: sol
**20. ตอบ [d)]{.ans}**

Accumulator มี register เดียว ค่ากลางจึงต้องเก็บลง memory บ่อย (memory traffic สูง) และ ACC เป็น bottleneck ไม่เหมาะกับ pipeline

- **ตัวลวง a:** กลับกัน คือ accumulator ใช้ hardware น้อยที่สุด
:::

::: sol
**21. ตอบ [a)]{.ans}**

สไลด์: "Intel ISA is considered CISC, but it is translated into internal RISC code before performing parallelism" เส้นแบ่งระหว่าง CISC กับ RISC จึงไม่ชัดอีกต่อไป
:::

::: sol
**22. ตอบ [d) 8]{.ans}**

double ขนาด 8 bytes ต้องเริ่มที่ address mod 8 = 0 → a อยู่ที่ 0, padding 1–7, **b อยู่ที่ 8–15**
:::

::: sol
**23. ตอบ [b) Strength reduction]{.ans}**

แทน operation ที่แพง (คูณ) ด้วย operation ที่ถูกกว่า (shift) เป็น machine-dependent optimization
:::

::: sol
**24. ตอบ [c) Relocatable]{.ans}**

ปลายทาง = PC + displacement ไม่ผูกกับ address จริง ย้ายโปรแกรมไปวางที่ไหนก็ยังถูก และ branch ส่วนใหญ่กระโดดใกล้ ๆ จึงใช้ field เล็กได้

- **ตัวลวง a:** PC-relative กระโดดได้แค่ในระยะของ field ไปทุก address ไม่ได้
:::

::: sol
**25. ตอบ [d)]{.ans}**

Callee-save: subroutine PUSH เฉพาะ register ที่จะใช้แล้ว POP ก่อน RET → ไม่ save เกินจำเป็น (สไลด์ถามว่า "Callee save has more benefit?")

- **ตัวลวง a:** เป็นแบบ caller-save หรือ PUSHA
:::

::: sol
**26. ตอบ [a)]{.ans}**

BEQ: alu_ops = 10 (SUB เพื่อดู zero), sel_addpc = zero, sel_b = 0 (เทียบกับ R[rt]), reg_wr = 0, mem_wr = 0

- **ตัวลวง b:** เป็นค่าของ ADD
- **ตัวลวง d:** เป็นค่าของ LW
:::

::: sol
**27. ตอบ [c) อ่าน 2, เขียน 1]{.ans}**

อ่าน R[rs] และ R[rt] พร้อมกันได้ แต่เขียนได้ทีละตัว ซึ่งเป็นต้นเหตุของ structural hazard เมื่อ 2 คำสั่ง WB พร้อมกันใน pipeline
:::

::: sol
**28. ตอบ [b) 825 ns]{.ans}**

ADD 4 × 4 = 16, SW 2 × 4 = 8, BEQ 2 × 3 = 6, JMP 1 × 3 = 3 → **33 cycles** × 25 = **825 ns**

- **ตัวลวง a:** นับแบบ single cycle (9 × 25)
- **ตัวลวง d:** คิดว่าทุกคำสั่งใช้ 5 cycles
:::

::: sol
**29. ตอบ [d)]{.ans}**

Microinstruction เป็นส่วนของ **organization** เปลี่ยนรุ่น CPU แล้วโปรแกรมใช้ไม่ได้ ส่วน ISA (macroinstruction) เป็น abstraction ที่ทำให้ software portable
:::

::: sol
**30. ตอบ [c)]{.ans}**

แก้ structural hazard ด้วยการ**เพิ่ม resource** ("make two copies") ให้มี I-cache สำหรับ IF และ D-cache สำหรับ MEM ทำงานพร้อมกันได้
:::

::: sol
**31. ตอบ [a) RAW]{.ans}**

b อ่าน a ซึ่ง**เพิ่งถูกเขียน** → Read After Write (ตัวอย่างตรงจากสไลด์) และแก้ได้ด้วย forwarding
:::

::: sol
**32. ตอบ [b) 1]{.ans}**

**Load-use:** ข้อมูลพร้อมตอนจบ MEM แต่คำสั่งถัดไปต้องใช้ตอนต้น EX ใน cycle เดียวกัน forward ย้อนเวลาไม่ได้ จึงต้อง stall 1 cycle

- **ตัวลวง d (3):** เป็นกรณีที่ไม่มี forwarding เลย
:::

::: sol
**33. ตอบ [c) 90%]{.ans}**

สไลด์: ทายแบบคงที่ได้อย่างน้อย 50% ส่วน "more advance scheme 90% correct (e.g. branch history)"
:::

::: sol
**34. ตอบ [a) 254]{.ans}**

T = (k + (n − x)/x) T<sub>c</sub> = 5 + 996/4 = 5 + 249 = **254**

- **ตัวลวง b (1004):** เป็น pipeline ธรรมดา
- **ตัวลวง c (250):** ลืมเวลา fill
:::

::: sol
**35. ตอบ [d)]{.ans}**

Dynamic scheduling จัดลำดับตอนรันด้วย hardware binary เดิมจึงได้ประโยชน์ทันที

- **ตัวลวง a, b, c:** เป็นข้อดีของ **static** scheduling ทั้งหมด
:::

::: sol
**36. ตอบ [b) Capacity]{.ans}**

สไลด์เรียก ping-pong effect ว่า "extreme capacity miss" (cache เล็กเกินกว่าจะเก็บ working set ได้)
:::

::: sol
**37. ตอบ [a)]{.ans}**

block ใหญ่เกินไปที่ cache size คงที่จะทำให้:
- จำนวน block น้อยลง → **temporal locality แย่ลง miss rate กลับเพิ่ม**
- block ใหญ่ขึ้น → **miss penalty สูงขึ้น** (ต้องย้ายข้อมูลมากขึ้นผ่าน bus เดิม)

**ตัวลวง d:** compulsory miss ยังมีอยู่เสมอ แม้ block ใหญ่จะช่วยลดลงได้บ้าง
:::

::: sol
**38. ตอบ [b) 4-way]{.ans}**

เงื่อนไข: cache size / ways ≤ page size → 16 KB / ways ≤ 4 KB → **ways ≥ 4**
:::

::: sol
**39. ตอบ [a)]{.ans}**

Miss penalty ของดิสก์สูงมาก ถ้า write-through ทุกการเขียนต้องไปถึงดิสก์ จึงใช้ write-back (page out ตอนถูก replace) เท่านั้น
:::

::: sol
**40. ตอบ [c) 16 TB]{.ans}**

RAID 6 เสียพื้นที่ให้ parity 2 ลูก: (6 − 2) × 4 = **16 TB** และทนดิสก์เสียได้ 2 ลูก

- **ตัวลวง b (20 TB):** คิดแบบ RAID 5
- **ตัวลวง a (24 TB):** คิดแบบ RAID 0
:::

## Part 2: ตอบสั้น

::: sol
**S1. [(ก) J = 1, K = X (ข) T = 1]{.ans}**

- JK: Q 0 → 1 ทำได้ทั้ง set (J = 1, K = 0) และ toggle (J = 1, K = 1) ดังนั้น **K เป็น don't care**
- T: ต้องการให้ค่าเปลี่ยน จึงใช้ **T = 1**

**เกณฑ์:** ข้อละ 1 คะแนน
:::

::: sol
**S2. [1101 1011 = 0xDB]{.ans}**

1. +37 = 0010 0101
2. กลับบิตได้ 1101 1010
3. บวก 1 ได้ **1101 1011 = 0xDB**

ตรวจ: 0xDB = 219 และ 219 − 256 = −37 ✓
:::

::: sol
**S3. [CPU time = 3 s, MIPS = 2000]{.ans}**

- T = 6 × 10⁹ × 1.25 / 2.5 × 10⁹ = 7.5/2.5 = **3 s**
- MIPS = IC / (T × 10⁶) = 6 × 10⁹ / 3 × 10⁶ = **2000** (ตรวจ: f / (CPI × 10⁶) = 2500/1.25 = 2000 ✓)
:::

::: sol
**S4. [A = 11.6 s, B = 10.2 s → เลือก B]{.ans}**

- A: 0.7 × 8 + 0.3 × 20 = 5.6 + 6.0 = **11.6**
- B: 0.7 × 12 + 0.3 × 6 = 8.4 + 1.8 = **10.2**

บทเรียน: A เร็วกว่าในโปรแกรมที่ใช้บ่อย (P1) แต่ช้ามากใน P2 จนเฉลี่ยแล้วแพ้ → "เร็วที่สุด" ขึ้นกับ workload
:::

::: sol
**S5. [little: 0D 0C 0B 0A, big ที่ 0x102 = 0x0C]{.ans}**

| Address | 0x100 | 0x101 | 0x102 | 0x103 |
|---|---|---|---|---|
| Little endian | **0D** | 0C | 0B | 0A |
| Big endian | 0A | 0B | **0C** | 0D |
:::

::: sol
**S6. [CPI = 4.05, multi-cycle เร็วกว่าเล็กน้อย]{.ans}**

1. CPI = 0.25(5) + 0.10(4) + 0.45(4) + 0.15(3) + 0.05(3) = 1.25 + 0.40 + 1.80 + 0.45 + 0.15 = **4.05**
2. เวลาต่อคำสั่ง: multi = 4.05 × 60 = **243 ns** และ single = 250 ns
3. → multi-cycle เร็วกว่า 250/243 ≈ **1.03 เท่า** (ต่างกันน้อยมาก)

เกณฑ์ตัดสิน: multi-cycle ชนะเมื่อ CPI < 250/60 ≈ 4.17
:::

::: sol
**S7. Dependencies + เหตุผลที่ย้าย SUB ไม่ได้**

| คู่ | Register | ชนิด |
|---|---|---|
| 1 → 2 | r2 | **RAW** (load-use → stall 1) |
| 2 → 4 | r3 | **RAW** (forward ได้) |
| 1 → 3 | r2 | **WAW** |
| 2 → 3 | r2 | **WAR** |

- **ทำไมย้ายไม่ได้:** ถ้าย้าย SUB ไปไว้ก่อน ADD จะทำให้ ADD อ่าน r2 ที่ SUB เขียน แทนค่าที่ LW โหลด (**ละเมิด WAR**) และค่าสุดท้ายของ r2 จะกลายเป็นค่าจาก LW แทน SUB (**ละเมิด WAW**) ผลลัพธ์จึงผิด
- **วิธีแก้:** **register renaming** โดยให้ SUB เขียนลง register อื่น (เช่น r7) และแก้คำสั่งหลังจากนั้นที่ใช้ r2 ให้ใช้ r7 แทน จากนั้นจึงย้าย SUB มาคั่นระหว่าง LW กับ ADD เพื่อลบ stall ได้

**เกณฑ์:** ระบุ dependency ครบ 1 คะแนน และอธิบายเหตุผลพร้อมวิธีแก้ 1 คะแนน
:::

::: sol
**S8. [tag 18, index 9, offset 5, ใช้ 2 comparators]{.ans}**

1. offset = log₂32 = 5
2. #sets = 32768 / (32 × 2) = 512 → index = 9
3. tag = 32 − 9 − 5 = 18
4. ใช้ 2 comparators (หนึ่งตัวต่อ way)
:::

::: sol
**S9. [แบบเดิม 6 cycles, 2-way 5.5 cycles → 2-way ดีกว่า]{.ans}**

- แบบเดิม: 2 + 0.08 × 50 = 2 + 4 = **6 cycles**
- 2-way: 2.5 + 0.06 × 50 = 2.5 + 3 = **5.5 cycles**

บทเรียน: associativity แลก hit time ที่เพิ่มขึ้นกับ miss rate ที่ลดลง ต้องคำนวณ AMAT จึงจะตัดสินได้
:::

::: sol
**S10. RAID กับดิสก์ 3 TB × 5**

| Level | พื้นที่ใช้งาน | เสียได้ |
|---|---|---|
| RAID 0 | 5 × 3 = **15 TB** | **0 ลูก** |
| RAID 5 | (5 − 1) × 3 = **12 TB** | **1 ลูก** |
| RAID 6 | (5 − 2) × 3 = **9 TB** | **2 ลูก** |

**เกณฑ์:** ถูกครบ 3 แถวได้ 2 คะแนน ถูก 2 แถวได้ 1 คะแนน
:::

## แปลผลชุดที่ 3–4 (เต็มชุดละ 60)

| คะแนน | ระดับ | ทำต่อ |
|---|---|---|
| 51–60 | พร้อมมาก | อ่านกับดักรวมใน Exam Notes ก่อนสอบ |
| 42–50 | พร้อม | ใช้ตาราง "ข้อไหนอยู่บทไหน" หาบทที่ผิด แล้วอ่านเฉพาะส่วนนั้น |
| 30–41 | ปานกลาง | อ่าน Exam Notes บทที่ผิดใหม่ แล้วทำชุดที่ทำผิดเยอะซ้ำ |
| < 30 | ต้องเร่ง | เริ่มจาก Formula Sheet แล้วไล่ตัวอย่างในแต่ละบท |
