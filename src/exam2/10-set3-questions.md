# ชุดที่ 3 (60 คะแนน, 90 นาที)

| ส่วน | จำนวน | คะแนน | Digital Logic | Computer Architecture |
|---|---|---|---|---|
| Part 1: Choice | 40 ข้อ × 1 | 40 | ข้อ 1–11 | ข้อ 12–40 |
| Part 2: ตอบสั้น | 10 ข้อ × 2 | 20 | S1–S2 | S3–S10 |
| **รวม** | | **60** | **15** | **45** |

## Part 1: Choice (ข้อละ 1 คะแนน)

### Digital Logic (ข้อ 1–11)

:::: q
**1.** (2B)₁₆ มีค่าเท่าใดในฐานสิบ

::: choices
a) 32

b) 43

c) 53

d) 211
:::
::::

:::: q
**2.** 25.625 ในฐานสิบ เขียนเป็นฐานสองได้ว่า

::: choices
a) 11001.101

b) 11001.011

c) 10011.101

d) 11010.101
:::
::::

:::: q
**3.** 1111 0110 ในระบบ 8-bit two's complement มีค่าเท่าใด

::: choices
a) −9

b) 246

c) −10

d) −118
:::
::::

:::: q
**4.** Sign-extend เลข 4-bit two's complement `1010` ให้เป็น 8 bits ได้ผลเป็น

::: choices
a) 0000 1010

b) 1000 1010

c) 1111 0101

d) 1111 1010
:::
::::

:::: q
**5.** การบวกเลข 8-bit two's complement คู่ใดเกิด **signed overflow**

::: choices
a) 0x7F + 0x01

b) 0x80 + 0x7F

c) 0xFF + 0x01

d) 0x40 + 0xC0
:::
::::

:::: q
**6.** A + A'B ลดรูปได้เป็น

::: choices
a) A

b) A + B

c) AB

d) A'B
:::
::::

:::: q
**7.** F(A,B,C) = Σm(1, 3, 5, 7) ลดรูปได้เป็น

::: choices
a) A

b) B'

c) C

d) A + C
:::
::::

:::: q
**8.** ฟังก์ชัน 3 ตัวแปร F = Σm(0, 1, 2) เขียนในรูป POS ได้เป็น

::: choices
a) ΠM(0, 1, 2)

b) ΠM(3, 4, 5, 6, 7)

c) ΠM(5, 6, 7)

d) Σm(3, 4, 5, 6, 7)
:::
::::

:::: q
**9.** Decoder 3-to-8 ได้รับอินพุต ABC = 101 output เส้นใดเป็น 1

::: choices
a) Y2

b) Y3

c) Y5

d) Y6
:::
::::

:::: q
**10.** T flip-flop มี Q = 1 และ T = 1 หลังขอบ clock ค่า Q คือ

::: choices
a) 0

b) 1

c) คงเดิม

d) ไม่แน่นอน (forbidden)
:::
::::

:::: q
**11.** FSM ที่มี 12 states ถ้าใช้ **one-hot encoding** ต้องใช้ flip-flop กี่ตัว

::: choices
a) 4

b) 6

c) 12

d) 24
:::
::::

### Computer Architecture (ข้อ 12–40)

:::: q
**12.** ข้อใด**ไม่ใช่**ส่วนประกอบของ Computer Organization ตามสไลด์

::: choices
a) ALU

b) Bus

c) Control Unit

d) Instruction format
:::
::::

:::: q
**13.** การที่ซอฟต์แวร์ของ 8088 ยังรันบน Core i7 ได้ แสดงถึงข้อใด

::: choices
a) Moore's Law

b) ISA เป็น abstraction of software for hardware (backward compatibility)

c) Core i7 มี organization เหมือน 8088

d) Amdahl's Law
:::
::::

:::: q
**14.** โปรแกรมเดิมใช้เวลา 10 s หลังปรับปรุงเหลือ 4 s ได้ speedup เท่าใด

::: choices
a) 0.4

b) 1.5

c) 2.5

d) 6
:::
::::

:::: q
**15.** การใช้ quicksort หรือ merge sort สั้น ๆ เป็นตัววัด performance จัดเป็น benchmark ประเภทใด

::: choices
a) Real

b) Kernel

c) Synthetic

d) Toy
:::
::::

:::: q
**16.** CPU 500 MHz รันโปรแกรม 2 × 10⁸ คำสั่ง ด้วย CPI เฉลี่ย 2.5 จะใช้ CPU time เท่าใด

::: choices
a) 0.1 s

b) 0.25 s

c) 1 s

d) 2.5 s
:::
::::

:::: q
**17.** เครื่องในข้อ 16 มีค่า MIPS เท่าใด

::: choices
a) 80

b) 200

c) 500

d) 1250
:::
::::

:::: q
**18.** โปรแกรมที่ทำ parallel ได้ 75% ของเวลา จะได้ speedup **สูงสุด**เท่าใด (cores → ∞)

::: choices
a) 1.33

b) 3

c) 4

d) ไม่มีขีดจำกัด
:::
::::

:::: q
**19.** ถ้ารู้สัดส่วนการใช้งานจริงของแต่ละโปรแกรม และต้องการรวม**เวลา**ที่วัดได้เป็นค่าเดียว ควรใช้ค่าเฉลี่ยแบบใด

::: choices
a) Weighted arithmetic mean

b) Geometric mean

c) Harmonic mean

d) Median
:::
::::

:::: q
**20.** สถาปัตยกรรมแบบใดคำนวณ x = (a·b) + (a − (b·c)) ได้ด้วย**คำสั่งน้อยที่สุด (4 คำสั่ง)** ตามสไลด์

::: choices
a) Memory-Memory (3 operands)

b) Load-Store

c) Stack

d) Accumulator
:::
::::

:::: q
**21.** เก็บค่า 0xDEADBEEF แบบ **little endian** ที่ address 0x40 ไบต์ที่ address 0x40 คือ

::: choices
a) 0xDE

b) 0xAD

c) 0xBE

d) 0xEF
:::
::::

:::: q
**22.** โค้ด C `A = **p;` ตรงกับ addressing mode ใด

::: choices
a) Register indirect

b) Memory indirect

c) Displacement

d) Auto-increment
:::
::::

:::: q
**23.** ข้อใดถูกต้องเกี่ยวกับ **unrestricted alignment**

::: choices
a) compiler ต้องใส่ padding ให้ทุกตัวแปร

b) hardware จะ trap ทุกครั้งที่ข้อมูลไม่ aligned

c) hardware ต้องตรวจและแก้เอง ซึ่งอาจต้องเข้าถึง memory 2 ครั้งขึ้นไป

d) เร็วกว่า restricted alignment เสมอ
:::
::::

:::: q
**24.** Exception ที่เกิดจาก**ซอฟต์แวร์** เช่น system call หรือการหารด้วยศูนย์ เรียกว่า

::: choices
a) Interrupt

b) Trap

c) Vector

d) Bubble
:::
::::

:::: q
**25.** การหา handler แบบ **Fixed Entry** ทำงานอย่างไร

::: choices
a) อ่าน address ของ handler จากตารางตามหมายเลข interrupt

b) กระโดดไปที่ Base + หมายเลข × ขนาด handler

c) กระโดดไป address คงที่เสมอ แล้วให้ software อ่าน interrupt-source register เพื่อตัดสินใจ

d) hardware เลือก handler ตาม priority เอง
:::
::::

:::: q
**26.** ใน nanoLADA single-cycle ค่า control ของคำสั่ง **LW** ข้อใดถูก

::: choices
a) sel_b = 1, sel_data = 1, reg_wr = 1

b) sel_b = 0, sel_data = 0, reg_wr = 1

c) sel_b = 1, sel_data = x, mem_wr = 1

d) sel_pc = 1, reg_wr = 0
:::
::::

:::: q
**27.** คำสั่ง nanoLADA ใดใช้ extender แบบ **zero extend**

::: choices
a) ORI

b) ORUI

c) LW

d) BEQ
:::
::::

:::: q
**28.** คำสั่ง `JMP` ใน nanoLADA มี address field = 0x40 ค่า PC ถัดไปคือ

::: choices
a) 0x40

b) 0x44

c) 0x100

d) 0x104
:::
::::

:::: q
**29.** ใน multi-cycle nanoLADA cycle ที่ 4 ของคำสั่ง **SW** ทำอะไร

::: choices
a) IR ← MEM[PC]

b) REG_S ← REG_A + REG_B

c) MEM[REG_S] ← REG_M

d) R[rt] ← REG_WR
:::
::::

:::: q
**30.** ซักผ้าแบบ pipeline 4 ขั้นที่ใช้เวลา 30, 40, 30, 20 นาที เมื่อ pipeline เต็มแล้วจะมีผ้าเสร็จ 1 load ทุกกี่นาที

::: choices
a) 20

b) 30

c) 40

d) 120
:::
::::

:::: q
**31.** Branch delay slot ต้องอาศัยสิ่งใดจึงจะได้ประโยชน์

::: choices
a) จำนวน register มากขึ้น

b) compiler ที่หาคำสั่งอิสระมาใส่ใน slot

c) TLB

d) write buffer
:::
::::

:::: q
**32.** วงจร hazard detection ของ pipeline เปรียบเทียบอะไร

::: choices
a) opcode ของคำสั่งที่ติดกัน

b) rs/rt ของคำสั่งปัจจุบัน กับ register ปลายทางที่รอเขียนของคำสั่งใน EX/MEM/WB

c) ค่า PC ของทุก stage

d) address ของ memory ที่กำลังอ่าน
:::
::::

:::: q
**33.** เทคนิคใด**กำจัด WAR และ WAW** ที่เกิดจาก out-of-order execution ได้

::: choices
a) Forwarding

b) Branch prediction

c) Register renaming

d) Write buffer
:::
::::

:::: q
**34.** VLIW เพิ่ม performance โดย**ลดตัวแปรใด**ใน CPU time เป็นหลัก

::: choices
a) IC

b) CPI

c) T<sub>c</sub>

d) Miss rate
:::
::::

:::: q
**35.** ข้อใดเป็นตัวอย่างของ SIMD

::: choices
a) Intel AVX

b) Server แบบ multicore

c) Uniprocessor 8088

d) ระบบ fault-tolerant ที่ให้หลายเครื่องคำนวณแล้ว vote
:::
::::

:::: q
**36.** ข้อใดเป็นตัวอย่างของ **temporal locality**

::: choices
a) อ่าน array เรียงจาก index 0 ไปเรื่อย ๆ

b) ตัวแปร i ใน loop ถูกใช้ซ้ำทุกรอบ

c) คำสั่งถูก fetch เรียงตาม address

d) block size 64 bytes
:::
::::

:::: q
**37.** 2-way set associative cache ขนาด 8 KB มี block size 32 bytes จะมีกี่ sets

::: choices
a) 64

b) 128

c) 256

d) 512
:::
::::

:::: q
**38.** Cache แบบ write-back ต้องมีบิตใดเพิ่มในแต่ละ line

::: choices
a) Parity bit

b) Dirty bit

c) Sign bit

d) Carry bit
:::
::::

:::: q
**39.** Page fault ถูกจัดการโดยใคร

::: choices
a) Cache controller

b) TLB

c) Operating system (software)

d) Compiler
:::
::::

:::: q
**40.** NAS ใช้ protocol ใดในการแชร์ไฟล์

::: choices
a) iSCSI

b) Fibre Channel

c) NFS

d) SATA
:::
::::

## Part 2: ตอบสั้น (ข้อละ 2 คะแนน)

### Digital Logic

::: q
**S1.** ต้องใช้ 2-input **NAND gate อย่างน้อยกี่ตัว**จึงจะสร้างฟังก์ชัน A + B ได้ และเขียนนิพจน์ที่ใช้

<div class="answer-line"></div>
:::

::: q
**S2.** ลดรูป F(A,B,C,D) = Σm(0, 2, 5, 7, 8, 10, 13, 15) ให้เป็น SOP ที่สั้นที่สุด

<div class="answer-line"></div>
:::

### Computer Architecture

::: q
**S3.** เครื่อง A และ B ใช้ ISA เดียวกัน (IC เท่ากัน) โดย A: 2 GHz, CPI 2.0 และ B: 3 GHz, CPI 2.7 เครื่องใดเร็วกว่า และเร็วกว่ากี่เท่า

<div class="answer-line"></div>
:::

::: q
**S4.** งาน floating-point กินเวลา 40% ของโปรแกรม ถ้าทำให้ FP เร็วขึ้น 5 เท่า overall speedup เป็นเท่าใด

<div class="answer-line"></div>
:::

::: q
**S5.** ระบบมี interrupt หมายเลข 6

- (ก) ถ้าใช้ **Vector Table** ที่ base 0x2000 และ address 32 bits CPU จะอ่าน address ของ handler จาก address ใด
- (ข) ถ้าใช้ **Handler Table** ที่ base 0x2000 และ handler ขนาด 64 bytes CPU จะกระโดดไปที่ address ใด

<div class="answer-line"></div>
:::

::: q
**S6.** ใช้ delay ของ single-cycle nanoLADA ตามสไลด์ (PC 10, Inst MEM 40, Control 40, Register 20, MUX 10, ALU 60, Data MEM 40, MUX 10 ns) คำสั่ง **ADD** ใช้เวลาจริงเท่าใด และ clock cycle ของเครื่องต้องตั้งเป็นเท่าใด

<div class="answer-line"></div>
:::

::: q
**S7.** 5-stage pipeline (full forwarding) cycle time 2 ns รัน 200 คำสั่ง โดย 10% ของคำสั่งเป็น load ที่มีคำสั่งถัดไปใช้ค่าทันที (load-use) และไม่มี stall อื่น จะใช้เวลาเท่าใด

<div class="answer-line"></div>
:::

::: q
**S8.** Direct-mapped cache ขนาด 4 KB, block 16 bytes, address 32 bits จงหา **index และ tag** (ฐานสิบ) ของ address 0x00001234

<div class="answer-line"></div>
:::

::: q
**S9.** CPU มี CPI<sub>ideal</sub> = 1.2 และ 25% ของคำสั่งเป็น load/store โดย I-cache miss rate 1%, D-cache miss rate 4% และ miss penalty 80 cycles จงหา CPI จริง

<div class="answer-line"></div>
:::

::: q
**S10.** Virtual address 32 bits, page size 16 KB และ PTE ขนาด 4 bytes จงหาจำนวนบิตของ **VPN** และ**ขนาดของ page table** ต่อ process

<div class="answer-line"></div>
:::

```{=html}
<div class="pagebreak"></div>
```
