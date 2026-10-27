# ชุดที่ 1: ข้อสอบเสมือนจริงตามเกณฑ์ (60 คะแนน, 90 นาที)

| ส่วน | จำนวน | คะแนน | Digital Logic | Computer Architecture |
|---|---|---|---|---|
| Part 1: Choice | 40 ข้อ × 1 | 40 | ข้อ 1–11 | ข้อ 12–40 |
| Part 2: ตอบสั้น | 10 ข้อ × 2 | 20 | S1–S2 | S3–S10 |
| **รวม** | | **60** | **15** | **45** |

## Part 1: Choice (ข้อละ 1 คะแนน)

### Digital Logic (ข้อ 1–11)

:::: q
**1.** (1011.01)₂ มีค่าเท่าใดในฐานสิบ

::: choices
a) 11.01

b) 11.25

c) 11.5

d) 13.25
:::
::::

:::: q
**2.** 0x3F7 มีค่าเท่าใดในฐานแปด

::: choices
a) 1767₈

b) 3767₈

c) 1773₈

d) 7731₈
:::
::::

:::: q
**3.** −100 ในระบบ 8-bit two's complement คือ

::: choices
a) 0x64

b) 0xE4

c) 0x9B

d) 0x9C
:::
::::

:::: q
**4.** ช่วงค่าของเลข 6-bit two's complement คือ

::: choices
a) −31 ถึง 31

b) −32 ถึง 31

c) −31 ถึง 32

d) 0 ถึง 63
:::
::::

:::: q
**5.** บวกเลข 8-bit two's complement 0x70 + 0x50 ข้อใดถูก

::: choices
a) carry out = 1, overflow = 1

b) carry out = 0, overflow = 0

c) carry out = 0, overflow = 1

d) carry out = 1, overflow = 0
:::
::::

:::: q
**6.** ข้อใดถูกต้องตามกฎ DeMorgan

::: choices
a) (AB)' = A'B'

b) (A + B)' = A' + B'

c) (AB)' = A' + B'

d) (A + B)' = AB
:::
::::

:::: q
**7.** F(A,B,C) = A'B'C' + A'B'C + AB'C' + AB'C ลดรูปได้เป็น

::: choices
a) A'

b) B'

c) B'C'

d) A + B'
:::
::::

:::: q
**8.** F(A,B,C,D) = Σm(0, 2, 8, 10) + d(1, 3, 9, 11) รูปที่ลดได้น้อยที่สุดคือ

::: choices
a) B'D'

b) A'B'

c) B'

d) B' + D'
:::
::::

:::: q
**9.** Multiplexer แบบ 32-to-1 ต้องมี select lines กี่เส้น

::: choices
a) 4

b) 5

c) 16

d) 32
:::
::::

:::: q
**10.** JK flip-flop ที่มี J = 1 และ K = 1 จะเกิดอะไรขึ้นที่ขอบ clock

::: choices
a) Q = 0

b) Q = 1

c) Q คงเดิม

d) Q กลับค่า (toggle)
:::
::::

:::: q
**11.** ข้อใดถูกต้องเกี่ยวกับ Moore machine

::: choices
a) output ขึ้นกับ state ปัจจุบันเท่านั้น

b) output ขึ้นกับ input ปัจจุบันเท่านั้น

c) ใช้ state น้อยกว่า Mealy เสมอ

d) output เขียนไว้บนเส้น transition
:::
::::

### Computer Architecture (ข้อ 12–40)

:::: q
**12.** Intel เพิ่ม L3 cache และ Hyper-Threading ใน CPU รุ่นใหม่ โดยโปรแกรมเดิมรันได้ทันทีไม่ต้อง compile ใหม่ นี่คือการเปลี่ยนแปลงในระดับใด

::: choices
a) ISA

b) ABI

c) Computer Organization

d) Compiler
:::
::::

:::: q
**13.** Moore's Law กล่าวว่า

::: choices
a) clock rate เพิ่มเป็น 2 เท่าทุก 2 ปี

b) จำนวน transistor บน IC เพิ่มเป็น 2 เท่าประมาณทุก 2 ปี (18 เดือน)

c) ราคา DRAM ลดลง 40% ต่อปี

d) performance เพิ่มขึ้นตามจำนวน core
:::
::::

:::: q
**14.** Computer A รันโปรแกรมใช้เวลา 15 s ส่วน Computer B ใช้ 24 s ข้อใดถูก

::: choices
a) A เร็วกว่า B 1.6 เท่า

b) A เร็วกว่า B 0.625 เท่า

c) B เร็วกว่า A 1.6 เท่า

d) A เร็วกว่า B 9 เท่า
:::
::::

:::: q
**15.** Computer X ทำ 4 งานพร้อมกันเสร็จทั้งหมดใน 8 นาที ส่วน Computer Y ทำทีละงาน งานละ 3 นาที ข้อใดถูก

::: choices
a) X มี throughput สูงกว่า และ Y มี response time ต่ำกว่า

b) Y ดีกว่าทั้งสองด้าน

c) X ดีกว่าทั้งสองด้าน

d) throughput เท่ากัน
:::
::::

:::: q
**16.** โปรแกรมมี 4 × 10⁹ คำสั่ง รันด้วย average CPI = 1.5 บน CPU 3 GHz จะใช้ CPU time เท่าไร

::: choices
a) 0.5 s

b) 1.125 s

c) 2 s

d) 8 s
:::
::::

:::: q
**17.** ส่วนของโปรแกรมที่กินเวลา 60% ถูกทำให้เร็วขึ้น 3 เท่า overall speedup คือ

::: choices
a) 1.67

b) 1.8

c) 2.0

d) 3.0
:::
::::

:::: q
**18.** เหตุผลที่ควรใช้ geometric mean กับผล benchmark ที่เป็น ratio คือ

::: choices
a) ได้ค่าเฉลี่ยมากที่สุด

b) ให้ผลสอดคล้องกันไม่ว่าจะใช้เครื่องใดเป็น baseline

c) ทำนายเวลาจริงได้แม่นยำ

d) ไม่ต้องใช้ workload
:::
::::

:::: q
**19.** สถาปัตยกรรมแบบใดเป็น "0-address" (operand อยู่ที่ top of stack โดยปริยาย)

::: choices
a) Accumulator

b) Stack

c) Register-Memory

d) Load-Store
:::
::::

:::: q
**20.** เก็บค่า 0x11223344 แบบ **big endian** ที่ address 0x1000 ไบต์ที่ address **0x1003** คือ

::: choices
a) 0x11

b) 0x22

c) 0x33

d) 0x44
:::
::::

:::: q
**21.** คำสั่ง `LD r1, 100(r2)` ที่ใช้อ่าน field ของ struct (เช่น `A = G.age`) ใช้ addressing mode ใด

::: choices
a) Register indirect

b) Displacement

c) Memory indirect

d) Scale
:::
::::

:::: q
**22.** ภายใต้ restricted alignment address ใดเก็บ `int` (4 bytes) ได้ถูกต้อง

::: choices
a) 0x1002

b) 0x1006

c) 0x100C

d) 0x1011
:::
::::

:::: q
**23.** ระบบใช้ **Handler Table** ที่ base 0x4000 โดย handler แต่ละตัวมีขนาด 32 bytes เมื่อเกิด interrupt หมายเลข 3 CPU จะกระโดดไปที่

::: choices
a) 0x400C

b) 0x4003

c) 0x4060

d) 0x4096
:::
::::

:::: q
**24.** ใน nanoLADA single-cycle ค่า control ของคำสั่ง `ADD rd, rs, rt` ข้อใดถูก

::: choices
a) sel_wr = 1 (rt), sel_b = 1 (imm)

b) sel_wr = 0 (rd), sel_b = 0 (R[rt])

c) sel_data = 1 (memory)

d) mem_wr = 1
:::
::::

:::: q
**25.** ขั้นตอนแรกของการออกแบบ processor ตามสไลด์คือ

::: choices
a) ประกอบ control logic

b) เลือก components ของ datapath

c) วิเคราะห์ ISA โดยเขียนแต่ละคำสั่งเป็น RTL

d) หา critical path
:::
::::

:::: q
**26.** single-cycle nanoLADA มี critical path 230 ns clock rate สูงสุดประมาณเท่าไร

::: choices
a) 230 MHz

b) 43.5 MHz

c) 4.35 MHz

d) 2.3 GHz
:::
::::

:::: q
**27.** multi-cycle nanoLADA (cycle time 20 ns) รันโปรแกรมที่มี LW 3 คำสั่ง, ADD 2 คำสั่ง และ BEQ 1 คำสั่ง จะใช้เวลาเท่าไร

::: choices
a) 120 ns

b) 480 ns

c) 520 ns

d) 600 ns
:::
::::

:::: q
**28.** ข้อดีสำคัญของการ implement control ด้วย microprogram คือ

::: choices
a) เร็วกว่า hardwired เสมอ

b) เปลี่ยน microprogram (Map ROM) แล้วทำ ISA อื่นบน hardware เดิมได้

c) ไม่ต้องมี state

d) ลด IC ของโปรแกรม
:::
::::

:::: q
**29.** ตัวอย่าง laundry มี 4 ขั้นตอน ขั้นละ 30 นาที ถ้าทำแบบ pipeline จำนวน **6 loads** จะใช้เวลาเท่าไร

::: choices
a) 3 ชั่วโมง

b) 4.5 ชั่วโมง

c) 6 ชั่วโมง

d) 12 ชั่วโมง
:::
::::

:::: q
**30.** ใน pipeline ที่ LW ใช้ 5 stages และ R-type ใช้ 4 stages (ไม่มี MEM) ถ้า LW ตามด้วย ADD ทั้งสองคำสั่งจะเขียน register file ใน cycle เดียวกัน นี่คือ hazard ชนิดใด

::: choices
a) Structural

b) Data (RAW)

c) Control

d) WAR
:::
::::

:::: q
**31.** โค้ด `a = sin(x); x = 10;` (โดยที่ sin ต้องเตรียมนาน) อาจเกิด hazard ชนิดใด

::: choices
a) RAW

b) WAW

c) WAR

d) RAR
:::
::::

:::: q
**32.** ตาม Flynn's taxonomy ในสไลด์ MISD ใช้กับงานแบบใด

::: choices
a) Uniprocessor

b) Vector processor

c) Fault-tolerant computing

d) Multicore
:::
::::

:::: q
**33.** Superpipeline ที่มี m = 3 minor cycles, k = 5 stages รัน n = 301 คำสั่ง (ideal) ใช้เวลาเท่าไร

::: choices
a) 105 T<sub>c</sub>

b) 305 T<sub>c</sub>

c) 101 T<sub>c</sub>

d) 903 T<sub>c</sub>
:::
::::

:::: q
**34.** ข้อใด**ไม่ใช่**ข้อจำกัดหรือข้อเสียของ loop unrolling

::: choices
a) code size ใหญ่ขึ้น

b) จำนวน register จำกัดจำนวนรอบที่ unroll ได้

c) ทำให้ basic block เล็กลง

d) ต้อง rename register เพื่อให้แต่ละ iteration อิสระกัน
:::
::::

:::: q
**35.** Fully associative cache ยังคงมี miss ชนิดใดบ้าง

::: choices
a) Conflict อย่างเดียว

b) Compulsory และ Capacity

c) Compulsory, Capacity และ Conflict

d) ไม่มี miss เลย
:::
::::

:::: q
**36.** Direct-mapped cache ขนาด 64 bytes มี block size 8 bytes address 300 (ฐานสิบ) จะอยู่ที่ index ใด

::: choices
a) 4

b) 5

c) 37

d) 44
:::
::::

:::: q
**37.** Write-through cache ที่ write buffer เต็มบ่อย (saturate) เพราะ memory ช้ามาก วิธีแก้ที่สไลด์เสนอคือ

::: choices
a) เพิ่มขนาด write buffer ไปเรื่อย ๆ

b) เพิ่ม L2 cache

c) ปิด cache

d) ใช้ direct-mapped
:::
::::

:::: q
**38.** TLB มักจัดเป็น fully associative เพราะ

::: choices
a) ขนาดใหญ่มาก

b) มีขนาดเล็ก (ประมาณ 128–256 entries) จึงเทียบทุก entry ได้

c) ไม่มี tag

d) OS จัดการทั้งหมด
:::
::::

:::: q
**39.** Virtual address 32 bits, page size 8 KB และ page table entry 4 bytes ขนาด page table ต่อ process คือ

::: choices
a) 1 MB

b) 2 MB

c) 4 MB

d) 8 MB
:::
::::

:::: q
**40.** RAID 5 ประกอบด้วยดิสก์ 2 TB จำนวน 4 ลูก จะมีพื้นที่ใช้งานจริงเท่าไร

::: choices
a) 2 TB

b) 4 TB

c) 6 TB

d) 8 TB
:::
::::

## Part 2: ตอบสั้น (ข้อละ 2 คะแนน)

ตอบเป็นตัวเลขพร้อมหน่วย หรือวลีสั้น ๆ

### Digital Logic

::: q
**S1.** เขียนสมการ Boolean ของ **Sum** และ **Carry-out** ของ full adder (อินพุต A, B, Cin)

<div class="answer-line"></div><div class="answer-line"></div>
:::

::: q
**S2.** ออกแบบ **Moore machine** ตรวจจับลำดับ "101" แบบ overlapping จะต้องใช้กี่ state และต้องใช้ flip-flop **อย่างน้อย**กี่ตัว (binary encoding)

<div class="answer-line"></div>
:::

### Computer Architecture

::: q
**S3.** โปรแกรมมี 2 × 10⁹ คำสั่ง รันบน CPU 2 GHz ด้วย instruction mix ดังนี้: ALU 40% (CPI 1), Load 30% (CPI 4), Store 10% (CPI 3), Branch 20% (CPI 2) จงหา **average CPI** และ **CPU time**

<div class="answer-line"></div>
:::

::: q
**S4.** ส่วนที่ปรับปรุงได้กินเวลา 90% ของโปรแกรม ต้องทำให้ส่วนนั้นเร็วขึ้นกี่เท่า จึงจะได้ overall speedup = 5

<div class="answer-line"></div>
:::

::: q
**S5.** ภายใต้ restricted alignment ตัวแปรถูกวางตามลำดับนี้โดยเริ่มที่ address 0: `char a; int b; short c; double d; char e;` ตัวแปร **d** เริ่มที่ address ใด และ**ไบต์สุดท้ายที่ใช้**คือ address ใด

<div class="answer-line"></div>
:::

::: q
**S6.** Single-cycle processor มี cycle time 200 ns ส่วน multi-cycle (nanoLADA: LW 5, SW 4, R-type/ORI 4, BEQ 3 cycles) มี cycle time 50 ns ถ้า instruction mix คือ LW 20%, SW 10%, R-type/ORI 50% และ BEQ 20% จงหา **average CPI ของ multi-cycle** และบอกว่าเครื่องไหนเร็วกว่า

<div class="answer-line"></div>
:::

::: q
**S7.** พิจารณา 5-stage pipeline ที่มี full forwarding ระบุ data dependency ทั้งหมด (ชนิดและ register) และบอกว่าต้อง stall กี่ cycle

```
1: LW  $r1, 0($r2)
2: ADD $r3, $r1, $r1
3: SW  $r3, 4($r2)
4: ADD $r1, $r4, $r5
```

<div class="answer-line"></div><div class="answer-line"></div>
:::

::: q
**S8.** ทำไม RAID 5 จึง**เขียน**ได้เร็วกว่า RAID 4 (ตอบ 1–2 ประโยค) และ RAID 5 ต้องใช้ดิสก์อย่างน้อยกี่ลูก

<div class="answer-line"></div><div class="answer-line"></div>
:::

::: q
**S9.** ระบบมี address 32 bits ใช้ **4-way set associative cache ขนาด 64 KB** โดย **block size 64 bytes** จงหาจำนวนบิตของ **tag, index และ offset**

<div class="answer-line"></div>
:::

::: q
**S10.** ระบบ cache 2 ระดับ: L1 hit time 1 cycle, L1 miss rate 4%, L2 hit time 12 cycles, L2 local miss rate 25% และ memory access 200 cycles จงหา **AMAT**

<div class="answer-line"></div>
:::
