# ชุดที่ 4 (60 คะแนน, 90 นาที)

| ส่วน | จำนวน | คะแนน | Digital Logic | Computer Architecture |
|---|---|---|---|---|
| Part 1: Choice | 40 ข้อ × 1 | 40 | ข้อ 1–11 | ข้อ 12–40 |
| Part 2: ตอบสั้น | 10 ข้อ × 2 | 20 | S1–S2 | S3–S10 |
| **รวม** | | **60** | **15** | **45** |

## Part 1: Choice (ข้อละ 1 คะแนน)

### Digital Logic (ข้อ 1–11)

:::: q
**1.** (1101 0110)₂ เขียนเป็นฐานสิบหกได้ว่า

::: choices
a) 0xD6

b) 0x6D

c) 0xC6

d) 0xD5
:::
::::

:::: q
**2.** 345₈ มีค่าเท่าใดในฐานสิบ

::: choices
a) 345

b) 229

c) 237

d) 197
:::
::::

:::: q
**3.** เลข **unsigned 10 bits** มีช่วงค่าเท่าใด

::: choices
a) 0 ถึง 1023

b) −512 ถึง 511

c) 0 ถึง 1024

d) 0 ถึง 511
:::
::::

:::: q
**4.** −90 ในระบบ 8-bit **one's complement** คือ

::: choices
a) 1010 0110

b) 1010 0101

c) 1101 1010

d) 0101 1010
:::
::::

:::: q
**5.** บวกเลข 8-bit two's complement 0x90 + 0xA0 ข้อใดถูก

::: choices
a) carry out = 0, overflow = 0

b) carry out = 1, overflow = 0

c) carry out = 0, overflow = 1

d) carry out = 1, overflow = 1
:::
::::

:::: q
**6.** A ⊕ B เท่ากับข้อใด

::: choices
a) AB + A'B'

b) A'B + AB'

c) (A + B)'

d) A'B'
:::
::::

:::: q
**7.** AB + A'C + BC ลดรูปได้เป็น

::: choices
a) AB + A'C

b) AB + BC

c) A + C

d) BC
:::
::::

:::: q
**8.** F(A,B,C) = Σm(0, 2, 4, 6) ลดรูปได้เป็น

::: choices
a) A'

b) C'

c) B'

d) A'C'
:::
::::

:::: q
**9.** ต้องใช้ MUX แบบ 2-to-1 กี่ตัวจึงจะสร้าง MUX แบบ 8-to-1 ได้

::: choices
a) 3

b) 4

c) 7

d) 8
:::
::::

:::: q
**10.** อุปกรณ์ใดเปลี่ยนค่าเฉพาะ**ที่ขอบ (edge)** ของ clock

::: choices
a) SR latch

b) D latch

c) D flip-flop

d) Combinational circuit
:::
::::

:::: q
**11.** **Mealy machine** ที่ตรวจจับลำดับ "101" แบบ overlapping ต้องใช้อย่างน้อยกี่ state

::: choices
a) 2

b) 3

c) 4

d) 5
:::
::::

### Computer Architecture (ข้อ 12–40)

:::: q
**12.** ในลำดับชั้นของ abstraction ชั้นใดอยู่ระหว่าง compiler/OS กับ hardware (datapath & control)

::: choices
a) ABI

b) ISA

c) Datapath

d) Layout
:::
::::

:::: q
**13.** Pipelining ปรับปรุงสิ่งใดเป็นหลัก

::: choices
a) Latency ของแต่ละคำสั่ง

b) Instruction count

c) Throughput

d) Miss penalty
:::
::::

:::: q
**14.** ในผลลัพธ์ของคำสั่ง `time` บน Unix ค่า **real** คือเวลาใด

::: choices
a) CPU time ใน user mode

b) CPU time ใน kernel

c) Elapsed (wall-clock) time

d) CPU time ของทุก process รวมกัน
:::
::::

:::: q
**15.** X ใช้เวลา 30 s และ Y ใช้เวลา 20 s กับโปรแกรมเดียวกัน Y เร็วกว่า X กี่เท่า

::: choices
a) 0.67

b) 1.5

c) 10

d) 50
:::
::::

:::: q
**16.** โปรแกรมหนึ่งใช้ 3 × 10⁹ clock cycles บน CPU 1.5 GHz จะใช้ CPU time เท่าใด

::: choices
a) 0.5 s

b) 3 s

c) 2 s

d) 4.5 s
:::
::::

:::: q
**17.** Instruction mix: 60% มี CPI 1, 30% มี CPI 2 และ 10% มี CPI 5 average CPI คือ

::: choices
a) 1.7

b) 2.67

c) 8

d) 1.5
:::
::::

:::: q
**18.** ทำให้ส่วนที่กินเวลา 50% เร็วขึ้น 2 เท่า จะได้ overall speedup เท่าใด

::: choices
a) 1.33

b) 1.5

c) 2

d) 1.25
:::
::::

:::: q
**19.** Speedup ของสองโปรแกรมคือ 2 และ 8 geometric mean คือ

::: choices
a) 4

b) 5

c) 16

d) 3.2
:::
::::

:::: q
**20.** ข้อใดเป็นข้อเสียของ **Accumulator architecture** ตามสไลด์

::: choices
a) ต้องใช้ register จำนวนมาก

b) decode ซับซ้อน

c) code density แย่ที่สุด

d) memory traffic สูง และ accumulator เป็น bottleneck
:::
::::

:::: q
**21.** ข้อใดอธิบายยุค **Post-RISC** ได้ถูกต้อง

::: choices
a) x86 แปลคำสั่ง CISC เป็นคำสั่งภายในคล้าย RISC (micro-ops) ก่อนทำ parallelism

b) RISC ถูกเลิกใช้ไปแล้ว

c) ARM กลายเป็น CISC

d) x86 เปลี่ยนเป็น fixed-length instruction
:::
::::

:::: q
**22.** ภายใต้ restricted alignment ถ้าประกาศ `char a; double b;` เริ่มที่ address 0 ตัวแปร b จะเริ่มที่ address ใด

::: choices
a) 1

b) 2

c) 4

d) 8
:::
::::

:::: q
**23.** compiler เปลี่ยน `x * 8` เป็น `x << 3` คือ optimization แบบใด

::: choices
a) Code motion

b) Strength reduction

c) Common subexpression elimination

d) Procedure inlining
:::
::::

:::: q
**24.** ข้อดีหลักของ branch แบบ **PC-relative** คือ

::: choices
a) กระโดดไป address ใดก็ได้ใน memory

b) ไม่ต้องใช้ adder

c) โปรแกรม relocatable (ย้ายไปวางที่ใดก็ทำงานได้)

d) ทำให้ memory เร็วขึ้น
:::
::::

:::: q
**25.** **Callee-save** หมายถึงข้อใด

::: choices
a) ผู้เรียก PUSH ทุก register ก่อน CALL

b) ไม่มีใคร save register

c) OS เป็นผู้ save register

d) subroutine save เฉพาะ register ที่ตัวเองจะแก้ แล้ว restore ก่อน RET
:::
::::

:::: q
**26.** ใน nanoLADA single-cycle ค่า control ของคำสั่ง **BEQ** ข้อใดถูก

::: choices
a) alu_ops = 10 (SUB), sel_addpc = zero, reg_wr = 0

b) alu_ops = 00, reg_wr = 1

c) sel_pc = 1, mem_wr = 1

d) sel_data = 1, reg_wr = 1
:::
::::

:::: q
**27.** Register file ของ nanoLADA มีกี่ port

::: choices
a) อ่าน 1, เขียน 1

b) อ่าน 2, เขียน 2

c) อ่าน 2, เขียน 1

d) อ่าน 3, เขียน 1
:::
::::

:::: q
**28.** multi-cycle nanoLADA (cycle time 25 ns) รัน ADD 4 คำสั่ง, SW 2 คำสั่ง, BEQ 2 คำสั่ง และ JMP 1 คำสั่ง จะใช้เวลาเท่าใด

::: choices
a) 225 ns

b) 825 ns

c) 900 ns

d) 1125 ns
:::
::::

:::: q
**29.** ทำไมจึงไม่ให้ programmer เขียนโปรแกรมด้วย microinstruction โดยตรง

::: choices
a) microinstruction ทำงานช้ากว่า

b) microinstruction ไม่ Turing complete

c) ต้องใช้ OS พิเศษ

d) microinstruction ผูกกับ organization ของแต่ละรุ่น จึงไม่ compatible ข้ามรุ่น
:::
::::

:::: q
**30.** ถ้ามี memory ตัวเดียวทั้งคำสั่งและข้อมูล pipeline จะเกิด structural hazard วิธีแก้ที่สไลด์เสนอคือ

::: choices
a) Forwarding

b) แทรก NOP เสมอ

c) แยก instruction cache กับ data cache

d) Branch prediction
:::
::::

:::: q
**31.** โค้ด `a = 7; b = a + 5;` เป็น dependency ชนิดใด

::: choices
a) RAW

b) WAR

c) WAW

d) Structural
:::
::::

:::: q
**32.** 5-stage pipeline ที่มี full forwarding ถ้า LW ตามด้วยคำสั่งที่ใช้ค่านั้นทันที ต้อง stall กี่ cycle

::: choices
a) 0

b) 1

c) 2

d) 3
:::
::::

:::: q
**33.** ตามสไลด์ branch prediction แบบใช้ branch history ทายถูกประมาณเท่าใด

::: choices
a) 50%

b) 75%

c) 90%

d) 100%
:::
::::

:::: q
**34.** Superscalar degree 4 กับ pipeline 5 stages รัน 1000 คำสั่ง (ideal) ใช้เวลากี่ T<sub>c</sub>

::: choices
a) 254

b) 1004

c) 250

d) 259
:::
::::

:::: q
**35.** ข้อดีของ **dynamic scheduling** (superscalar OoO) เทียบกับ static scheduling คือ

::: choices
a) hardware ง่ายกว่า

b) compiler เห็น scope กว้างกว่า

c) ใช้ power ต่ำกว่า

d) software เดิมเร็วขึ้นบน hardware ใหม่โดยไม่ต้อง recompile
:::
::::

:::: q
**36.** "Ping-pong effect" (cache มี 1 line ทุก address ใหม่ miss หมด) เป็นกรณีสุดโต่งของ miss ชนิดใด

::: choices
a) Compulsory

b) Capacity

c) Conflict

d) Coherence
:::
::::

:::: q
**37.** ถ้า cache size คงที่แต่เพิ่ม block size มากเกินไป จะเกิดอะไรขึ้น

::: choices
a) จำนวน block น้อยลง temporal locality แย่ลง miss rate กลับเพิ่ม และ miss penalty สูงขึ้น

b) miss rate ลดลงเสมอ

c) hit time เป็นศูนย์

d) ไม่มี compulsory miss อีกต่อไป
:::
::::

:::: q
**38.** page size 4 KB และต้องการ L1 cache ขนาด 16 KB ที่ทำ overlapped cache & TLB access ได้ ต้องใช้ associativity อย่างน้อยเท่าใด

::: choices
a) 2-way

b) 4-way

c) 8-way

d) 16-way
:::
::::

:::: q
**39.** ทำไม virtual memory จึงใช้ write-back เท่านั้น

::: choices
a) write-through ไปยังดิสก์ช้าและแพงเกินไป

b) ดิสก์เขียนข้อมูลไม่ได้

c) OS ติดตาม dirty page ไม่ได้

d) TLB บังคับไว้
:::
::::

:::: q
**40.** RAID 6 ที่ใช้ดิสก์ 4 TB จำนวน 6 ลูก มีพื้นที่ใช้งานจริงเท่าใด

::: choices
a) 24 TB

b) 20 TB

c) 16 TB

d) 12 TB
:::
::::

## Part 2: ตอบสั้น (ข้อละ 2 คะแนน)

### Digital Logic

::: q
**S1.** ถ้าต้องการให้ flip-flop เปลี่ยนจาก Q = 0 เป็น Q⁺ = 1 ต้องป้อนอินพุตอะไรให้ (ก) **JK flip-flop** (ค่า J, K) และ (ข) **T flip-flop**

<div class="answer-line"></div>
:::

::: q
**S2.** เขียน −37 ในระบบ 8-bit two's complement เป็นเลขฐานสองและฐานสิบหก

<div class="answer-line"></div>
:::

### Computer Architecture

::: q
**S3.** โปรแกรมมี 6 × 10⁹ คำสั่ง CPI 1.25 รันบน CPU 2.5 GHz จงหา **CPU time** และ **MIPS**

<div class="answer-line"></div>
:::

::: q
**S4.** มีโปรแกรม 2 ตัว ใช้งานจริงในสัดส่วน P1 70% และ P2 30% เวลาที่วัดได้ (วินาที) คือ Machine A: P1 = 8, P2 = 20 และ Machine B: P1 = 12, P2 = 6 จงหา **weighted arithmetic mean** ของแต่ละเครื่อง และบอกว่าควรเลือกเครื่องใด

<div class="answer-line"></div>
:::

::: q
**S5.** เก็บค่า 0x0A0B0C0D ที่ address 0x100 แบบ **little endian** จงเขียนค่าของ byte ที่ address 0x100, 0x101, 0x102, 0x103 และบอกว่าถ้าเป็น **big endian** byte ที่ 0x102 คืออะไร

<div class="answer-line"></div>
:::

::: q
**S6.** Single-cycle มี cycle time 250 ns ส่วน multi-cycle nanoLADA มี cycle time 60 ns โดย instruction mix คือ LW 25%, SW 10%, R-type/ORI 45%, BEQ 15%, JMP 5% จงหา **average CPI** ของ multi-cycle และบอกว่าเครื่องใดเร็วกว่า

<div class="answer-line"></div>
:::

::: q
**S7.** พิจารณาโค้ดบน 5-stage pipeline ที่มี full forwarding ระบุ dependency ทั้งหมด (ชนิดและ register) และอธิบายว่า**ทำไมย้าย SUB มาไว้ระหว่างคำสั่ง 1 กับ 2 เพื่อลด stall ไม่ได้** และต้องทำอย่างไรจึงจะย้ายได้

```
1: LW  $r2, 0($r1)
2: ADD $r3, $r2, $r4
3: SUB $r2, $r5, $r6
4: SW  $r3, 4($r1)
```

<div class="answer-line"></div><div class="answer-line"></div>
:::

::: q
**S8.** 2-way set associative cache ขนาด 32 KB, block 32 bytes, address 32 bits จงหาจำนวนบิตของ **tag, index, offset** และจำนวน comparator

<div class="answer-line"></div>
:::

::: q
**S9.** Cache เดิมมี hit time 2 cycles, miss rate 8%, miss penalty 50 cycles ถ้าเปลี่ยนเป็น 2-way ทำให้ miss rate ลดเหลือ 6% แต่ hit time เพิ่มเป็น 2.5 cycles จงหา AMAT ของทั้งสองแบบ และบอกว่าแบบใดดีกว่า

<div class="answer-line"></div>
:::

::: q
**S10.** มีดิสก์ 3 TB จำนวน 5 ลูก จงหาพื้นที่ใช้งานจริงและจำนวนดิสก์ที่เสียได้โดยข้อมูลไม่หาย สำหรับ **RAID 0, RAID 5 และ RAID 6**

<div class="answer-line"></div>
:::

```{=html}
<div class="pagebreak"></div>
```
