# Computer Architecture: Exam Notes (ฉบับเตรียมสอบจริง)

**อ้างอิง:** สไลด์ *Computer Architecture: Design and Analysis* (Krerk Piromsopa, Ph.D.) จากไฟล์ `com_arch_pdf_combined.pdf` ทั้ง 397 หน้า

> **ต่างจากสรุปของ GPT ตรงไหน**
> 1. **ลำดับบทเป็นของสไลด์จริง** สไลด์ไม่มีบท "Computer Arithmetic / Floating-point" ส่วน Chapter 4 คือ **Single Cycle Processor (nanoLADA)** และ Chapter 5 คือ **Multiple Cycle Processor**
> 2. ใส่**ตัวอย่างและตัวเลขที่อยู่ในสไลด์**ทุกข้อ เช่น critical path 230 ns, CPI 5/4/3 ของ multi-cycle, สูตร superscalar/VLIW, tag/index ของ cache และขนาด page table เพราะข้อสอบมักเอามาจากตรงนี้
> 3. ทุก Exercise ท้ายบทมี**เฉลยพร้อมวิธีทำ**
> 4. มีกล่อง ⚠️ **กับดัก** สำหรับจุดที่นักศึกษาทำผิดบ่อย

ไฟล์ในชุดนี้:
- `01-exam-notes.md` (ไฟล์นี้): สรุปเนื้อหาครบทุกบท
- `02-mock-exam.md`: ข้อสอบเสมือนจริง 90 นาที (ยังไม่มีเฉลย ให้ลองทำก่อน)
- `03-mock-exam-answers.md`: เฉลยละเอียดพร้อมวิธีคิด

---

## สารบัญ

| บท (ตามสไลด์) | หัวข้อ | น้ำหนักที่น่าจะออก |
|---|---|---|
| Ch 1 | Introduction | ★ (นิยาม, ISA vs Organization) |
| Ch 2 | Performance | ★★★ (คำนวณแน่นอน) |
| Ch 3 | Instruction Set Architecture | ★★★ (endian, alignment, addressing mode, ISA classes) |
| Ch 4 | Single Cycle Processor (nanoLADA) | ★★★ (RTL, control table, critical path) |
| Ch 5 | Multiple Cycle Processor | ★★ (physical RTL, จำนวน cycle, FSM, microprogram) |
| Ch 6 | Pipelining part 1 + 2 | ★★★ (hazards, forwarding, delay slot, reschedule) |
| Ch 7 | Contemporary Architecture (ILP) | ★★ (Flynn, superscalar/VLIW formula, loop unroll) |
| Ch 8 | Memory part 1 (Cache) + part 2 (Virtual Memory) | ★★★ (tag/index, AMAT, miss types, TLB) |
| Ch 9 | Storage Architecture | ★★ (RAID levels, SAN vs NAS) |
| — | Formula Sheet + Exercise Solutions | |

---

# Chapter 1: Introduction to Computer Architecture

### 1.1 ทำไมต้องเรียน
- Architecture ของ desktop/server **converged** แล้ว (ตลาดถูกกำหนดโดยเจ้าใหญ่) แต่ใต้ ISA เดิมมี **organizational innovation** มหาศาล
  - ตัวอย่างในสไลด์: **Core i3 / i5 / i7 ต่างกันที่ organization** (จำนวน core, cache, clock/Turbo Boost, Hyper-Threading) **ไม่ได้ต่างที่ ISA**
- เหตุผลที่ควรรู้: เพื่อออกแบบหรือ**เลือก** architecture ให้เหมาะ และเพื่อเป็น**นักพัฒนาที่ดีขึ้น**
- โปรแกรมสองตัวที่ใช้ algorithm เดียวกัน ภาษาเดียวกัน และเครื่องเดียวกัน ยังเร็วไม่เท่ากันได้ เพราะ data structure, compiler หรือ optimization ต่างกัน ("Good knowledge of architecture means better program")
  - ตัวอย่างในสไลด์: ใช้ `union` ที่รวม `unsigned short h[2]` เข้ากับ `unsigned int x` แล้วบวก `c.x = a.x + b.x` **ครั้งเดียวได้ผลสองค่า** (SIMD แบบบ้าน ๆ) ผลลัพธ์อาจต่างไปตาม compiler/OS

### 1.2 Computer Architecture = หลายระดับของ abstraction
Application → OS → Compiler → **Instruction Set Architecture** → Firmware → Instr. Set Processor / I/O system → **Datapath & Control** → Digital Design → Circuit Design → Layout

เอกสารที่อธิบาย computer architecture ควรมีอย่างน้อย **ISA, Computer Organization, ABI (Application Binary Interface)**

### 1.3 ISA vs Organization

| | **ISA** | **Computer Organization** |
|---|---|---|
| คืออะไร | abstraction ระหว่าง SW กับ HW | โครงสร้างภายในที่ทำให้ ISA ทำงานได้ |
| ใครเห็น | programmer/compiler | hardware designer |
| ตัวอย่าง | instruction, register, addressing, format, interrupt | ALU, Control Unit, Register, Bus, Memory subsystem, I/O subsystem |

- ISA เป็น **abstraction of machine for software**: เขียน C แล้ว compiler แปลเป็น binary โดยไม่ต้องรู้ hardware
- ISA เป็น **abstraction of software for hardware**: **โปรแกรม 8088 รุ่นเก่ายังรันบน Core i7 ได้** (backward compatibility)

### 1.4 ทำไมต้องมี Register
เทียบกับการบวก 2+3 สมัยประถม: จำ 2 ไว้ในหัว (temporary storage) ชู 3 นิ้ว แล้วนับ 3, 4, 5 → register คือ "ที่จำชั่วคราว" ใกล้หน่วยคำนวณ ทำให้ไม่ต้องไป memory ทุกครั้ง

### 1.5 Design Trade-offs / Goals
- **Cost vs Performance (vs Power)** ซึ่งต้องอาศัย modeling และ measurement
- Goals: functional requirements (market/application driven), performance goals, cost constraints, power constraints
- เกี่ยวข้องทั้ง ISA, Organization และ Hardware (logic design, packaging)
- **Requirements** ได้แก่ application area (general purpose, scientific, commercial, multimedia), OS requirements (memory management, security/protection, context switching, interrupts), standards (IEEE floating point, PCI, USB) และ time to market
- **Software trends:** ใช้ memory เพิ่มขึ้นประมาณ **2 เท่าต่อปี** (≈ เพิ่ม address 1 bit ต่อปี) และใช้ compiler มากขึ้น (ISA ออกแบบเพื่อ compiler ไม่ใช่เพื่อ programmer)
- **Hardware trends:** DRAM capacity เพิ่ม **4 เท่าทุก 3 ปี** แต่ performance ดีขึ้นช้า, Disk capacity เพิ่ม 4 เท่าทุก 3 ปี

### 1.6 Trends & Cost
- **Moore's Law:** เป็นข้อสังเกตของ Gordon Moore (co-founder ของ Fairchild และ CEO ของ Intel) ว่าจำนวน transistor บน IC **เพิ่มเป็นสองเท่าประมาณทุก 2 ปี (18 เดือน)**
- **ราคา DRAM ลดลงประมาณ 40% ต่อปี** เพราะ commoditization
- **Watts per MIPS** ดีขึ้นเรื่อย ๆ
- **ต้นทุนชิ้นส่วนของ notebook:** processor/circuit 25%, battery 25%, monitor 20%, storage 20%, RAM 10%, case 6% ฯลฯ โดยมี margin 20–30%+

### 1.7 How to design
เป็นกระบวนการ **iterative**: Creativity → Design → Cost/Performance Analysis → คัด bad/mediocre ideas ออก แล้ววนซ้ำ ใช้ **measurement & evaluation**

---

# Chapter 2: Performance: Measurement and Analysis

### 2.1 นิยาม
- Performance **ขึ้นกับบริบท (relative)** และเป็น **ส่วนกลับของ Execution Time**

$$\text{Performance} = \frac{1}{\text{Execution Time}} \qquad \text{"X เร็วกว่า Y n เท่า"} \Rightarrow n = \frac{T_Y}{T_X}$$

- n > 1 แปลว่าเร็วกว่า ส่วน n < 1 แปลว่าช้ากว่า
- ตัวอย่าง: A ใช้ 20 s และ B ใช้ 25 s → A เร็วกว่า B **25/20 = 1.25 เท่า**

> ⚠️ **กับดัก:** ห้ามคิดเป็น 20/25 = 0.8 หรือ (25−20)/25 = 20% ถ้าโจทย์ถาม "กี่เท่า" ให้ใช้ **เวลาของตัวช้า ÷ เวลาของตัวเร็ว** เสมอ

### 2.2 Response Time vs Throughput
- **Response Time** มีสองแบบ: **Elapsed (wall clock)** กับ **CPU time** (ไม่รวมเวลารอ I/O) วัดได้ด้วยคำสั่ง `time` ของ Unix (real / user / sys) ส่วน Windows ใช้ `ptime`
- **Throughput** = จำนวนงานต่อหน่วยเวลา หรือก็คือ parallelism ระดับ task
- ตัวอย่างในสไลด์:
  - Computer A ทำ 5 งานพร้อมกันเสร็จใน 10 นาที → throughput 0.5 task/min, response time 10 นาที
  - Computer B ทำทีละงาน งานละ 3 นาที → throughput 0.33 task/min, response time 3 นาที
  - → **A มี throughput ดีกว่า แต่ B มี response time ดีกว่า**
- **ส่ง 20 TB ด้วย fiber 1 Gb/s** ใช้เวลาประมาณ 40+ ชั่วโมง (20×8×10¹² / 10⁹ = 160,000 s ≈ 44 h) แต่**คนแบก HDD 20 ลูกเดินข้ามตึกใช้ 15 นาที** → คนแบกมี **throughput สูงกว่า** (ถึงแม้ fiber ส่ง bit แรกถึงเร็วกว่า)
- **MIPS** และ **FLOPS** เป็น "หน่วยเชิงการตลาด" ที่**ไม่ใช่ performance จริง**

### 2.3 Measurement Issues
**What to measure** (จะรันโปรแกรมอะไร), **Interference** (เครื่องว่างหรือมีงานอื่นรันอยู่), **Reproducibility** (วัดซ้ำได้ไหม), **Comparability** (A เก่ง multimedia ส่วน B เก่งงานอื่น แล้วตัวไหนดีกว่า?)

### 2.4 Benchmark 5 ประเภท
| ประเภท | ความหมาย |
|---|---|
| **Real** | ใช้ application จริง (มี script จำลองการใช้งานแบบ interactive/multi-user) |
| **Microbenchmark** | ใช้ส่วนหนึ่งของซอฟต์แวร์ |
| **Kernel** | วัดเฉพาะบางแง่มุมของ performance |
| **Toy** | โปรแกรมเล็ก ๆ เช่น quicksort หรือ merge sort (นิยมในอดีต) |
| **Synthetic** | เลียนแบบพฤติกรรมของโปรแกรมจริง เช่น **Whetstone, Dhrystone** |

**SPEC** (Standard Performance Evaluation Corporation, SPEC.org) มี SPEC CPU2017 (CPU), SPECviewperf (graphics), SPECjbb2015 (JVM), SPEC SFS2014 (file server) → ต้องใช้ **ชุด benchmark เดียวกัน (unified set)** จึงจะเทียบกันได้

### 2.5 การรวมผล: Arithmetic, Weighted และ Geometric Mean
ตัวอย่างในสไลด์ (เวลาเป็นวินาที):

| | A | B | C |
|---|---|---|---|
| Program 1 (weight 80%) | 10 | 4 | 5 |
| Program 2 (weight 20%) | 2 | 10 | 5 |
| Total | 12 | 14 | **10** |
| Arithmetic Mean | 6 | 7 | **5** |
| Weighted AM (0.8, 0.2) | 8.4 | 5.2 | **5** |

- Weighted AM ของ A = 0.8(10) + 0.2(2) = 8.4 และของ B = 0.8(4) + 0.2(10) = 5.2
- **"เร็วที่สุด"** ขึ้นกับ workload: ถ้า workload ตรงกับ weight นี้ C ดีสุด (5) แต่ถ้ารันแต่ Program 1 B จะดีสุด
- **ถ้าเป็น ratio (normalized/speedup ซึ่งไม่มีหน่วย) ให้ใช้ Geometric Mean**

$$GM = \sqrt[n]{\prod_{i=1}^n r_i}$$

| | A/B | A/C | C/B |
|---|---|---|---|
| Prog 1 | 10/4 = 2.5 | 10/5 = 2 | 5/4 = 1.25 |
| Prog 2 | 2/10 = 0.2 | 2/5 = 0.4 | 5/10 = 0.5 |
| **GM** | √0.5 = **0.71** | √0.8 = **0.89** | √0.625 = **0.79** |

- จุดเด่นของ GM คือ **consistent ไม่ว่าจะใช้เครื่องไหนเป็น baseline**: GM(A/B) / GM(A/C) = 0.71/0.89 = 0.79 = GM(C/B)
- **ข้อดี:** speedup + GM ทำให้ **ไม่ต้องสนใจขนาด workload** (ปรับจาก 5 s เป็น 3 s มีค่าเท่ากับปรับจาก 500 s เป็น 300 s)
- **ข้อเสีย:** **GM (และ speedup) ทำนาย performance จริงไม่ได้**

### 2.6 CPU Time (สูตรหลัก จำให้ขึ้นใจ)

$$\boxed{\text{CPU Time} = IC \times CPI \times T_c = \frac{IC \times CPI}{\text{Clock Rate}}}$$

- CPI = **Clock (cycles) Per Instruction** และ T_c = 1/clock rate
- RISC มักมี CPI คงที่ (เช่น 1)
- **Average CPI** เมื่อแต่ละ class มี CPI ต่างกัน:

$$CPI_{avg} = \sum_i CPI_i \times \frac{IC_i}{IC_{total}} \quad(\text{ถ่วงด้วยความถี่})$$

**ตัวแปรแต่ละตัวขึ้นกับอะไร** (สไลด์ Ch4 "Design Concept"):

| ตัวแปร | ขึ้นกับ |
|---|---|
| Instruction Count | Program, ISA, Compiler |
| CPI | ISA, CPU Organization (และ compiler บ้าง) |
| Clock Cycle Time | CPU Organization, VLSI Technology |

**วิธีลด CPU time (Performance Improvement):**
- ลด IC: redesign ISA, compiler optimization
- ลด CPI: redesign ISA, redesign CPU organization
- ลด cycle time: redesign organization, ใช้ transistor technology ที่เร็วขึ้น

**ตัวอย่างในสไลด์:** CPU 1 GHz รัน 2000 ล้านคำสั่งใน 20 s ถ้าเพิ่ม clock เป็น 2 GHz แต่ CPI แย่ลง 1.2 เท่า จะใช้เวลาเท่าไร?
- CPI_เดิม = (20 × 10⁹) / (2000 × 10⁶) = **10**
- CPI_ใหม่ = 10 × 1.2 = 12
- T_ใหม่ = (2000×10⁶ × 12) / (2×10⁹) = **12 s**

> ⚠️ "lower average CPI by a factor of 1.2" ในสไลด์หมายถึง **CPI แย่ลง (เพิ่มขึ้น) 1.2 เท่า** ดูจากที่เฉลยคิด 10 × 1.2

### 2.7 MIPS เป็นหน่วยวัดที่ไม่ดี

$$MIPS = \frac{IC}{T \times 10^6} = \frac{\text{Clock Rate}}{CPI \times 10^6}$$

**ตัวอย่างในสไลด์:** A = 10 MIPS @ 33 MHz, B = 9 MIPS @ 20 MHz ถ้าโปรแกรมเดียวกันใช้ 12M คำสั่งบน A และ 10M คำสั่งบน B
- T_A = 12×10⁶ / 10×10⁶ = **1.2 s**
- T_B = 10×10⁶ / 9×10⁶ = **1.11 s**
- → **B เร็วกว่า ทั้งที่ MIPS ต่ำกว่า** เพราะ ISA ต่างกันทำให้ IC ต่างกัน MIPS จึงเทียบข้าม ISA ไม่ได้

### 2.8 Amdahl's Law ("Law of diminishing returns")

$$\boxed{\text{Overall Speedup} = \frac{1}{(1-P) + \dfrac{P}{n}}} \qquad S_{max} = \frac{1}{1-P}\ (n\to\infty)$$

P = **สัดส่วนของเวลา** (ไม่ใช่สัดส่วนของคำสั่ง!) ที่ถูกเร่ง และ n = speedup ของส่วนนั้น

- **ตัวอย่างการซื้อของ:** มี 2 ส่วนคือ เดินทาง (A, ส่วนใหญ่ของเวลา) กับ ซื้อของ (B) → **ทำ A เร็วขึ้น 2 เท่าได้ผลดีกว่าทำ B เร็วขึ้น 5 เท่า** เพราะ A กินเวลามากกว่า → **"Make the common case fast"**
- **ตัวอย่างซื้ออาหาร:** การซื้อกินเวลา 1/3 ของเวลามื้ออาหาร ถ้าทำให้เร็วขึ้น 3 เท่า → 1/(2/3 + 1/9) = 9/7 ≈ **1.29**

**เฉลย Exercises ท้าย Ch2:**
1. **Mail server:** computation 40% เร็วขึ้น 10 เท่า (I/O 60%) → 1/(0.6 + 0.4/10) = 1/0.64 = **1.5625**
2. **FP เร็วขึ้น 1.6 เท่า** โดย FP กินเวลาครึ่งหนึ่ง → 1/(0.5 + 0.5/1.6) = 1/0.8125 = **1.23**
3. **FP 25%, CPI_FP = 4.0, CPI_อื่น = 1.33, ลด CPI_FP เหลือ 2.5**
   - CPI_เดิม = 0.25(4) + 0.75(1.33) = 1 + 0.9975 ≈ **2.0**
   - CPI_ใหม่ = 0.25(2.5) + 0.9975 = **1.6225**
   - Speedup = 2.0/1.6225 ≈ **1.23** (IC และ clock เท่าเดิมจึงตัดทิ้งได้)

> ⚠️ ข้อ 3 ห้ามใช้ Amdahl โดยแทน P = 25% เพราะ 25% เป็น**ความถี่ของคำสั่ง ไม่ใช่สัดส่วนของเวลา** สัดส่วนเวลาจริงของ FP คือ 1.0/2.0 = 50% ถ้าแทนให้ถูก 1/(0.5 + 0.5/(4/2.5)) = 1.23 ก็ได้คำตอบเท่ากัน

---

# Chapter 3: Instruction Set Architecture

### 3.1 ประวัติของวิชา
50s–60s เน้น Computer Arithmetic → 70s–80s เน้น ISA design และ ISA for compiler (Pascal, Ada, stack frame) → 90s เน้น CPU organization, memory, ISA extension (MMX, GPU) → 2000s เน้น parallelism, multi-core, 64-bit, PCIe, USB → 2010s เน้น GPU/deep learning, virtualization

### 3.2 ISA คือสิ่งที่ต้องรู้เพื่อเขียน assembly
1. **Instructions/Operators** (RTL, CPI, format)
2. **Operands, Registers, Flags**
3. **Memory reference** (addressing, referencing, dereferencing)
4. **Instruction format** (การ encode เป็น binary)
5. **Interrupt & Exception handler**

- **ปี 1964 IBM ออก IBM 360** ซึ่งรวม instruction set 7 แบบเป็นหนึ่งเดียว ก่อนหน้านั้นโปรแกรม **ไม่ portable**
- Anatomy ของ assembly: `label: OPCODE dest, src1, src2/#immediate` และ `[100]` คือ memory ที่ address 100

```
main: ORI $r1, $r0, #10   ; r1 = 10  ($r0 = 0)
      ORI $r2, $r0, #20
      ADD $r3, $r1, $r2
      SD  $r3, [100]      ; C = 10+20
```

### 3.3 Design Issues ของ ISA
- Operand เก็บที่ไหน: **accumulator, stack, registers, memory**
- มี explicit operand กี่ตัว: **0, 1, 2 หรือ 3**
- ระบุ operand อย่างไร: **addressing mode**

**คุณสมบัติของ ISA ที่ดี (ISA Matrix):** Compatibility (software portable), Generality/Completeness, **Orthogonal** (special case น้อย ใช้ทุก addressing mode กับทุก data type ได้), **Regularity** (ไม่ overload ความหมายของ field), Ease of compilation, Ease of implementation

### 3.4 ISA 5 แบบ (สำคัญมาก) ทุกแบบคำนวณ `x = (a*b) + (a – (b*c))`

| แบบ | ยุค | #address | จำนวนคำสั่ง | Pros | Cons |
|---|---|---|---|---|---|
| **Accumulator** | ก่อน 1960 | 1 (ACC เป็น implicit) | **11** | HW น้อยมาก ออกแบบง่าย | ACC เป็น bottleneck, ไม่เหมาะกับ parallelism/pipeline, memory traffic สูง |
| **Stack** | 1960s–70s | 0 (ใช้ top of stack) | **10** | HW น้อย, **code density ดี**, compiler ง่าย | stack เป็น bottleneck, ข้อมูลไม่ได้อยู่ top เสมอ, optimize ยาก, ไม่เหมาะกับ pipeline |
| **Memory-Memory** | 1970s–80s | 2–3 | **4** (3-op) / **7** (2-op) | คำสั่งน้อย, compiler ง่าย | **memory traffic สูงมาก**, CPI แปรผัน, แบบ 2-op ต้องย้ายข้อมูลเยอะ |
| **Register-Memory** | 1970s–ปัจจุบัน (x86) | 2 | **10** | ใช้ข้อมูลใน memory ได้โดยไม่ต้อง load, encode ง่าย, code density ดี | **ไม่ orthogonal** (operand ไม่เท่าเทียมกัน), CPI แปรผัน, อาจจำกัดจำนวน register |
| **Register-Register (Load-Store)** | 1960s–ปัจจุบัน (RISC) | 3 | **8** | **fixed-length encode ง่าย, CPI ใกล้เคียงกัน, pipeline ง่าย** | IC สูงกว่า, ต้องพึ่ง compiler ที่ดี |

ตัวอย่าง Stack:
```
PUSH a; PUSH b; MUL; PUSH a; PUSH b; PUSH c; MUL; SUB; ADD; POP x   (10 คำสั่ง)
```
ตัวอย่าง Load-Store:
```
LD r1,a; LD r2,b; LD r3,c; MUL r4,r1,r2; MUL r5,r2,r3; SUB r6,r1,r5; ADD r7,r4,r6; SD r7,x  (8 คำสั่ง)
```

**ประวัติ:** สมัยก่อน DRAM เร็วเมื่อเทียบกับ CPU และ transistor แพง จึงนิยม ISA ที่ใช้ memory เยอะ

### 3.5 CISC vs RISC
- **CISC** มีคำสั่งที่ทรงพลัง (complex) ส่วน **RISC** มีคำสั่งเป็น building block พื้นฐาน
- เมื่อ ILP (pipeline) เข้ามา **RISC ชนะ**
- ปัจจุบันเป็นยุค **Post-RISC**: Intel (CISC) **แปลคำสั่งเป็น RISC ภายใน (micro-ops)** ก่อนทำ parallelism → เส้นแบ่งไม่ชัดแล้ว
- **ARM = Acorn RISC Machine** ประหยัดพลังงาน (ใช้ใน mobile)

### 3.6 Memory Organization
- Memory คือ array ขนาดใหญ่ที่ index ด้วย address และใช้ **byte addressing** (ถ้าต้องการ bit ให้ใช้ mask ด้วย AND/OR)
- sizeof ใน C: char 1, short 2, int 4, long 8, float 4, double 8, long double 16

**Endian** (ข้อมูลหลาย byte อ้างอิงด้วย base address = address ต่ำสุด):
- **Little endian:** byte ต่ำ (LSB) อยู่ address ต่ำ เช่น **Intel**
- **Big endian:** byte สูง (MSB) อยู่ address ต่ำ เช่น **IBM PowerPC, Sun**; ไฟล์ **Photoshop** เก็บแบบ big endian เสมอ
- **ARM (ตั้งแต่ ARM6)** เลือกได้ทั้งสองแบบ (bi-endian)

เก็บ `0x1A2B3C4D`:

| Address | 00 | 01 | 02 | 03 |
|---|---|---|---|---|
| Big | 1A | 2B | 3C | 4D |
| Little | 4D | 3C | 2B | 1A |

**Endian กับ performance** (กรณี bus เล็กกว่าข้อมูล ซึ่งจะอ่านจาก address ต่ำไปสูง):
- **บวกเลข → little endian ดีกว่า** เพราะได้ byte ต่ำก่อน จึงบวกและส่ง carry ต่อได้ตามลำดับ
- **เปรียบเทียบมาก/น้อย → big endian ดีกว่า** เพราะได้ byte สูง (มี sign bit) ก่อน จึงตอบได้ทันที

**Alignment:**
- **Restricted alignment:** `Base Address mod size = 0`
  - ภาระอยู่ที่ **software/compiler**
  - HW ตรวจเจอ misalignment แล้ว **trap**
  - **ไม่เสียเวลาเพิ่ม** → **ชนะในแง่ performance ("make the common case fast")**
- **Unrestricted alignment:**
  - software ง่าย แต่ **HW ต้องตรวจและแก้เอง**
  - มักต้องเข้าถึง memory **2 ครั้งขึ้นไป** ทำให้ช้าและ logic แพง
  - บางครั้งต้องมีเพื่อ backward compatibility

**ตัวอย่างวาง memory แบบ restricted alignment** (Exercise): `char a; short b; int c; char d; long e; double f;`

| Addr | 0 | 1 | 2–3 | 4–7 | 8 | 9–15 | 16–23 | 24–31 |
|---|---|---|---|---|---|---|---|---|
| | a | pad | b | c | d | pad (7 B) | e | f |

รวม **32 bytes** (ถ้าจัดลำดับตัวแปรใหม่จากใหญ่ไปเล็กจะเหลือ 8+8+4+2+1+1 = 24 bytes)

### 3.7 Addressing Modes (10 แบบ ต้องจำตัวอย่าง C ที่คู่กันให้ได้)

| # | Mode | ตัวอย่าง | ความหมาย / C |
|---|---|---|---|
| 1 | Immediate | `LDI $r1, #4` | A = 4 |
| 2 | Register (direct) | `ADD $r1,$r2,$r3` | A = B + C |
| 3 | **Displacement** | `LD $r1, 100($r2)` | A = D[100] หรือ A = G.age (field ใน struct) |
| 4 | Register Indirect | `LD $r1, ($r2)` | A = *p |
| 5 | Index | `LD $r1, ($r2+$r3)` | A = D[i] |
| 6 | Direct (absolute) | `LD $r1, 1000` | อ่าน memory ที่ address 1000 (ตัวแปร global) |
| 7 | Memory Indirect | `LD $r1, @($r2)` | A = **p |
| 8 | Auto-increment | `LD $r1, ($r2)+` | A = D[i++] |
| 9 | Auto-decrement | `LD $r1, ($r2)-` | A = D[i--] |
| 10 | Scale | `LD $r1, ($r2)[$r3*4]` | F = E[i] (int ขนาด 4 bytes) |

- **register indirect ทดแทน mode อื่นได้เกือบทั้งหมด** (คำนวณ address ใส่ register ก่อน)
- **Trend สำหรับ ISA ใหม่:** รองรับ **displacement, immediate และ register indirect** โดย displacement field **12–16 bits** และ immediate field **8–16 bits** ส่วน mode ซับซ้อนให้ compiler แปลงเป็น mode ง่าย

### 3.8 ประเภทคำสั่ง
**Data movement** (LW, SW) / **Arithmetic** (Add, Sub, Mul, Div) / **Logic** (And, Or, Xor, Not) / **Control** (JMP, BEQ ซึ่งเปลี่ยน PC) / **Extended** (Multimedia, Encryption)

### 3.9 Control Flow
- Branch displacement มักเป็น **PC-relative** เพราะทำให้โปรแกรม **relocatable** (ย้ายไปวางที่ใดก็ทำงานได้) และ branch ส่วนใหญ่กระโดดใกล้ ๆ
- ถ้า address ไม่รู้ตอน compile (เช่น **shared library / dynamic binding**) ให้ใช้ register ที่เก็บ address เช่น `CALL $r14`

**Subroutine call:**
1. ส่ง parameter
2. save status
3. save return address
4. เปลี่ยน PC
5. ทำงาน
6. save return data

ขากลับ: restore status แล้ว load return address ไปที่ PC ทั้งหมดนี้กำหนดไว้ใน **ABI**

**Parameter passing:** ผ่าน **Register** (เร็ว) หรือ **Stack frame** (`PUSH #5; PUSH #4; CALL _min` แล้ว callee อ่าน `[$r14+4]`)

**Caller-save vs Callee-save:**
- **Caller save:** ผู้เรียก PUSH register ที่ตัวเองใช้ก่อน CALL แต่ caller **ไม่รู้ว่า callee ใช้ register ไหน** จึงอาจ save เกินจำเป็น
- **Callee save:** ตัว subroutine PUSH เฉพาะ register ที่ตัวเองจะแก้ → **มักมีประโยชน์กว่า** (save เท่าที่ต้องใช้)
- x86 มี `PUSHA/POPA` ที่ save ทุก register ซึ่ง**ง่ายแต่ช้า**

### 3.10 Exceptions
- **Exception = unprogrammed control flow**
  - Hardware/external = **Interrupt**
  - Software = **Trap**
  - Intel ใช้คำว่า interrupt กับทั้งสองแบบ
- ขั้นตอนคล้าย subroutine: save status → save PC → call handler → restore status → restore PC

**หา handler อยู่ที่ไหน (3 แบบ):**

| แบบ | เก็บอะไรในตาราง | วิธีหา |
|---|---|---|
| **Vector Table** | **address** ของ handler | `addr = mem[Base + (source# × address size)]` เช่น base 0x8000, int 8, 32-bit → **mem[0x8000 + 8×4] = mem[0x8020]** แล้วกระโดดไปที่ค่านั้น |
| **Handler Table** | **ตัว code** ของ handler (ขนาดคงที่) | `addr = Base + (source# × handler size)` เช่น handler 16 B, int 8 → **0x8000 + 8×16 = 0x8080** |
| **Fixed Entry** | ไม่มีตาราง | CPU กระโดดไป **0x1000 เสมอ** แล้ว software อ่าน interrupt-source register เพื่อตัดสินใจเอง |

### 3.11 Instruction Format
- การ encode มีผลต่อ **ขนาด code** และ **งาน decode**
- **Variable length** (x86): bits แรกบอกความยาว รองรับ mode เยอะ → code เล็ก
- **Fixed length** (nanoLADA, MIPS): mode น้อย opcode บอก mode → code ใหญ่ แต่ decode ง่าย
- **Hybrid:** ARM Thumb
- **เพื่อ performance แล้ว fixed length ชนะ**
- ตัวอย่าง: **code ของ MIPS ใหญ่ประมาณ 2 เท่าของ VAX แต่ CPI ของ MIPS เป็น 1/6 ของ VAX** → T_MIPS/T_VAX = 2 × 1/6 = 1/3 → **MIPS เร็วกว่าประมาณ 3 เท่า** (ถ้า clock เท่ากัน)

### 3.12 Compiler & Optimization
- Goals ของ compiler: **correctness**, speed of code, compile time, debugging support
- ขั้นตอน: front-end (language → intermediate) → high-level opt → global opt → code generator

| ระดับ | Optimization |
|---|---|
| High-level | **Procedure integration (inlining)** |
| Local (ภายใน basic block) | common subexpression elimination, constant propagation, stack height reduction |
| Global (ข้าม basic block) | global CSE, **copy propagation**, **code motion** |
| Machine-dependent | **strength reduction** (ใช้ shift แทนคูณ), branch offset opt, **pipeline scheduling** |

**Basic block** = ลำดับคำสั่งที่ไม่มี jump/branch อยู่ข้างใน

ตัวอย่าง:
- copy/constant propagation: `m=60; h=60*m; d=24*h; days=seconds/d;` → `days = seconds/86400;`
- CSE: `a=b+c+d; y=b+c+e;` → `x=b+c; a=x+d; y=x+e;`

**ข้อสังเกตเรื่องประสิทธิผลของ optimization:**
- โปรแกรม "locally simple, globally complex"
- **bug ส่วนใหญ่ของ compiler มาจาก optimization**
- **Alias (pointer) ทำให้เอาตัวแปรไปเก็บใน register ไม่ได้**

**ช่วย compiler writer:** Regularity (orthogonal), Simplicity (**ให้ primitives ไม่ใช่ solutions**), simplify trade-offs, allow compile-time binding

**Exercises:**
- **Clear register:** `CLR`, `MOV R1,0`, `SUB R1,R1,R1`, `XOR R1,R1,R1` → **XOR แนะนำที่สุด** (ไม่ต้องใช้ immediate, encode สั้น, HW รู้จัก idiom นี้)
- **Optimize loop:**
  ```c
  hs=3600; ds=86400;          // code motion: ค่าคงที่ย้ายออกนอก loop (และ constant folding 3600*24)
  for(x=0;x<=100;x++){ h=a[x]/hs; d=a[x]/ds; }
  ```
  หรือเขียน `d = h/24` ไม่ได้ เพราะเป็นการหารจำนวนเต็ม `a/86400 = (a/3600)/24` ซึ่งถูกเมื่อ a ≥ 0 แต่ต้องระวัง
- **Copy propagation `A=B+C; B=A+C; D=A-B;`**
  - → `A=B+C; B=B+C+C; D=(B+C)-(B+C+C)` ซึ่ง simplify ได้เป็น `D = -C`
  - บางคำสั่งมีงานเพิ่มขึ้น (B ต้องบวก 2 ครั้ง) บางคำสั่งลดลงมาก (D เหลือแค่ negate)
  - → optimization ไม่ได้ลดงานเสมอ compiler ต้องชั่งน้ำหนัก (เป็นปัญหาที่ยาก)

---

# Chapter 4: Single Cycle Processor (nanoLADA)

### 4.1 Concept
- Processor design (datapath + control) เป็นตัวกำหนด **CPI และ clock cycle time**
- **Single cycle:** CPI = 1 เริ่มคำสั่งใหม่ทุก cycle และทุก operation ของคำสั่งเป็น **combinational logic** → **cycle time ยาวมาก (ช้า)**

### 4.2 Design Steps (5 ขั้น ออกสอบบ่อย)
1. **วิเคราะห์ ISA** หา datapath requirements โดยเขียนแต่ละคำสั่งเป็น **RTL** และระบุ storage elements
2. **เลือก components** ของ datapath และกำหนด clocking methodology
3. **ประกอบ datapath** ให้ตรงกับ requirements (เพิ่มทีละคำสั่ง)
4. **วิเคราะห์แต่ละคำสั่ง** เพื่อหาค่า **control points**
5. **ประกอบ control logic**

### 4.3 nanoLADA ISA: fixed length 32-bit, 3 formats

| Format | Fields |
|---|---|
| **R-type** | opcode **6** · rs **5** · rt **5** · rd **5** · reserved **11** |
| **I-type** | opcode 6 · rs 5 · rt 5 · **immediate 16** |
| **J-type** | opcode 6 · **address/displacement 26** |

| Instr | Type | Opcode | RTL |
|---|---|---|---|
| `ORI rt, rs, imm` | I | 010000 | R[rt] ← R[rs] \| **zero_ext**(imm); PC ← PC+4 |
| `ORUI rt, rs, imm` | I | 010001 | R[rt] ← R[rs] \| **zero_pad**(imm); PC ← PC+4 |
| `ADD rd, rs, rt` | R | 000001 | R[rd] ← R[rs] + R[rt]; PC ← PC+4 |
| `LW rt, imm(rs)` | I | 011000 | R[rt] ← MEM[R[rs] + **sign_ext**(imm)]; PC ← PC+4 |
| `SW rt, imm(rs)` | I | 011100 | MEM[R[rs] + sign_ext(imm)] ← R[rt]; PC ← PC+4 |
| `BEQ rs, rt, imm` | I | 100100 | if R[rs]==R[rt]: PC ← PC + 4 + sign_ext(imm)×4 else PC ← PC+4 |
| `JMP addr` | J | 110000 | PC ← addr × 4 |

> **Extender 3 แบบ:** **Sign extend** (เติมด้วย sign bit, ใช้กับ LW/SW/BEQ), **Zero extend** (เติม 0 ข้างหน้า → 0x0000_imm, ใช้กับ ORI), **Zero pad** (imm อยู่ 16 บิตบนแล้วเติม 0 ข้างหลัง → imm_0000, ใช้กับ ORUI ทำหน้าที่แบบ "load upper")
>
> ตัวอย่าง: `ORUI $r1,$r0,#0x1234` → $r1 = 0x12340000 และ `ORI $r1,$r1,#0x5678` → $r1 = 0x12345678 (สร้างค่าคงที่ 32 บิตได้ด้วย 2 คำสั่ง)

### 4.4 Components
- **Register file:** **32 registers × 32 bit** (address 5 bit), **read 2 ports** (Read_A, Read_B), **write 1 port** สร้างจาก 32×32 D-FF + MUX + decoder
- **PC** (special register), **ALU** (ADD/OR/SUB), **Adder สำหรับ PC**, **Extender**
- **Memory:** 32-bit data, 32-bit address, 1 read port, 1 write port
- **ALU ops:** `00` S=A+B, `01` S=A|B, `10` S=A−B (BEQ ใช้ SUB แล้วดู flag **zero**)
- **Fetch:** Instruction ← MEM[PC]; PC ← PC+4
  - PC+4 = `{PC[31:2]+1, 2'b00}` → ใช้ **adder 30 bit** ก็พอ (2 bit ล่างเป็น 0 เสมอเพราะ word aligned)

### 4.5 Control Signals (ตารางนี้ควรจำได้หรือเข้าใจพอจะสร้างเองได้)
ความหมายของแต่ละสัญญาณ:
- `sel_pc`: 0 = PC ปกติ, 1 = JMP addr
- `sel_addpc`: 0 = PC+4, 1 = PC+4+imm×4
- `sel_wr`: 0 = เขียนลง rd, 1 = เขียนลง rt
- `sel_b`: 0 = ALU B มาจาก R[rt], 1 = มาจาก imm
- `sel_data`: 0 = เขียนผล ALU (S), 1 = เขียนข้อมูลจาก Memory
- `reg_wr`, `mem_wr`: 1 = เขียน
- `alu_ops`

| Instr | sel_pc | sel_addpc | sel_wr | sel_b | sel_data | reg_wr | mem_wr | alu_ops |
|---|---|---|---|---|---|---|---|---|
| ORI | 0 | 0 | 1 (rt) | 1 (imm) | 0 | **1** | 0 | 01 (OR) |
| ORUI | 0 | 0 | 1 | 1 | 0 | **1** | 0 | 01 |
| ADD | 0 | 0 | **0 (rd)** | **0 (reg)** | 0 | **1** | 0 | 00 |
| LW | 0 | 0 | 1 | 1 | **1 (mem)** | **1** | 0 | 00 (คำนวณ address) |
| SW | 0 | 0 | x | 1 | x | 0 | **1** | 00 |
| BEQ | 0 | **= zero** | x | 0 | x | 0 | 0 | **10 (SUB)** |
| JMP | **1** | x | x | x | x | 0 | 0 | xx |

> สังเกต: ค่า `x` (don't care) อยู่ในตำแหน่งที่คำสั่งนั้น**ไม่เขียน register** (SW/BEQ/JMP จึง don't care sel_wr และ sel_data) ส่วน **reg_wr และ mem_wr ห้ามเป็น x เด็ดขาด** เพราะจะเขียนทับข้อมูลผิดได้

**Control implementation:** Combinational logic / **ROM** / **PLA**

ใน PLA ให้ Gi เป็น AND term ของ opcode แต่ละตัว (G1 = ORI ... G7 = JMP) แล้ว:
- `sel_pc = G7`
- `sel_addpc = G6·zero`
- `sel_wr = G1+G2+G4`
- `sel_b = G1+G2+G4+G5`
- `sel_data = G4`
- `reg_wr = G1+G2+G3+G4`
- `mem_wr = G5`

### 4.6 Critical Path (**คำสั่งที่ยาวที่สุดคือ LW**)
| Step | เวลา |
|---|---|
| PC (clk-to-Q) | 10 |
| Instruction memory | 40 |
| Control/Decode | 40 |
| Register file read | 20 |
| MUX (sel_b) | 10 |
| ALU | 60 |
| Data Memory | 40 |
| MUX (sel_data) | 10 |
| **รวม** | **230 ns** |

- **Exercise:** benchmark 2 ล้านคำสั่ง → CPU time = 2×10⁶ × 1 × 230 ns = **0.46 s**
- **สรุป:** nanoLADA ง่ายเพราะมีคำสั่งน้อย เป็น fixed length และ immediate กับ displacement ใช้ field เดียวกัน **CPI = 1 แต่ cycle ยาว**
- **Scale addressing (Exercise):** การเพิ่ม `LD $r1, ($r2)[$r3*4]` ต้องมี **shifter (<<2) ที่ R[rt]** แล้วเข้า ALU บวกกับ R[rs] ต้องเพิ่ม MUX และ control signal ใหม่ และ critical path อาจยาวขึ้น

---

# Chapter 5: Multiple Cycle Processor

### 5.1 ปัญหาของ Single Cycle
- **Cycle time ยาว** และ**ทุกคำสั่งต้องรอนานเท่าคำสั่งที่ช้าที่สุด** (critical path)
- Memory จริงไม่ได้สวยงาม ต้องใช้หลาย cycle
- **Physical rule:** fast memories are small และ large memories are slow (ตอนนี้สมมติว่ามี cache ทำให้ memory = 1 cycle)

### 5.2 วิธีลด Cycle Time
- **แบ่ง combinational dependency graph แล้วใส่ intermediate register (latch)**
- ใช้หลาย cycle ที่เร็ว แทนที่จะใช้ cycle เดียวที่ช้า
- **บางคำสั่ง skip บาง cycle ได้** (นี่คือจุดที่ได้เปรียบ)
- **แต่ละส่วนควรใช้เวลาใกล้เคียงกัน** (balanced) เพราะ cycle time = max(stage)

5 ส่วน: **Fetch** (IR←MEM[PC]; PC←PC+4) → **Decode** (A←R[rs]; B←R[rt]/imm) → **Execute** (S←A op B) → **Memory** (Data←MEM[S]) → **Write back** (R[rt]←Data)

### 5.3 Physical RTL และจำนวน cycle ของแต่ละคำสั่ง (**ต้องจำ**)

| Instr | Cycles | ขั้นตอน |
|---|---|---|
| ORI / ORUI | **4** | IR←MEM[PC], PC←PC+4 · A←R[rs], B←ext(imm) · S←A\|B · R[rt]←S |
| ADD | **4** | Fetch · A←R[rs], B←R[rt] · S←A+B · R[rd]←S |
| **LW** | **5** | Fetch · A←R[rs], B←sign_ext · S←A+B · WR←MEM[S] · R[rt]←WR |
| SW | **4** | Fetch · A, B←sign_ext, **M←R[rt]** · S←A+B · MEM[S]←M |
| BEQ | **3** | Fetch · decode · if equal: PC ← PC + sign_ext(imm)×4 (PC ถูกบวก 4 ไปแล้วตอน fetch) |
| JMP | **3** | Fetch · decode · PC ← addr×4 |

**Design steps ของ multi-cycle:** ISA analysis → Components → Assemble datapath → **Datapath + Logical RTs → Physical RTs** → Physical RTs → Control

ปรับ datapath ได้อีก เช่น **ใช้ ALU บวก PC แทน adder แยก** และ**รวม instruction/data memory เป็นอันเดียว** (เพราะใช้คนละ cycle จึงแชร์ได้)

### 5.4 Control = Finite State Machine
- States: **Fetch → Decode →** { ALU_Exec → WB | ADD_Calc → MEM → (WB) | BEQ | JMP } → Fetch
- อาจต้องเพิ่ม **wait state** รอ memory ที่ไม่ ideal
- **Implementation:** **Sequential circuit** (state assignment + next-state truth table) หรือ **Microprogram**
  - **Microprogram:** มี microsequencer และ microinstruction แต่ละตัวระบุ control signals
  - map macroinstruction (assembly) ตัวหนึ่งเป็นหลาย microinstruction
  - **เปลี่ยน microprogram (Map ROM) ได้ = ทำ ISA อื่นบน HW เดิมได้**
- **CISC ทำให้ control ซับซ้อนกว่า**

### 5.5 Exercises Ch5
- **Potential speedup:** single cycle 210 ns, multi-cycle 45 ns → ให้ performance อย่างน้อยเท่าเดิม
  - CPI × 45 ≤ 210 → **CPI ≤ 4.67**
- **นับ cycle** (cycle time 40 ns):

  | Instr | Cycles |
  |---|---|
  | `LW $r2,0($r3)` | 5 |
  | `LW $r3,4($r3)` | 5 |
  | `BEQ` (not taken) | 3 |
  | `ADD` | 4 |
  | `SW` | 4 |

  รวม **21 cycles × 40 ns = 840 ns**
- **Share ALU กับ PC adder:** ใส่ MUX หน้า ALU input A (PC หรือ REG_A) และ input B (4 หรือ REG_B หรือ imm×4) แล้วให้ fetch cycle ใช้ ALU คำนวณ PC+4 ซึ่งทำได้เพราะ fetch ไม่ได้ใช้ ALU ทำอย่างอื่น
- **รองรับ interrupt/exception:** เพิ่ม register **EPC** (เก็บ PC), register **Cause/Status**, เพิ่ม state ใน FSM สำหรับตรวจ exception แล้วเปลี่ยน PC ไป handler (vector/fixed entry) และมีคำสั่ง return (IRET)
- **ทำไมไม่เขียนโปรแกรมด้วย microinstruction โดยตรง:**
  - microinstruction ผูกกับ **organization** (ไม่ใช่ ISA) เปลี่ยนรุ่น CPU แล้ว **โปรแกรมพัง (ไม่ compatible)**
  - microcode ยาวและกว้างมาก code density แย่
  - ISA เป็น abstraction ที่ทำให้ software portable

---

# Chapter 6: Pipelining

## Part 1

### 6.1 Concept: Laundry
- 4 คน (Ann, Brian, Cathy, Dave) และ 4 ขั้นตอน (wash, dry, fold, stash) ขั้นละ 30 นาที
- **Sequential: 4 × 4 × 0.5 = 8 ชั่วโมง** ส่วน **Pipelined: 3.5 ชั่วโมง**
- **Pop quiz: k loads** = เวลาเติม pipe + (k−1) × 30 นาที = 4(0.5) + (k−1)(0.5) = **(k+3)/2 ชั่วโมง** (k=4 ได้ 3.5 ✓)

**Lessons learned:**
1. **Pipelining ไม่ได้ลด latency ของแต่ละงาน** แต่ช่วย **throughput** ของ workload ทั้งหมด
2. หลายงานรันพร้อมกันบน **resource ต่างกัน**
3. **ความเร็วของ pipeline ถูกจำกัดด้วย stage ที่ช้าที่สุด**
4. **Stage ยาวไม่เท่ากัน ทำให้ speedup ลดลง**
5. **เวลา fill และ drain ทำให้ speedup ลดลง**

### 6.2 Potential Speedup
- Multi-cycle: T = n × 5 × T_c (ถ้าทุกคำสั่งใช้ 5 cycles)
- Pipeline: T = (**k** + (n − 1)) × T_c โดย k = จำนวน stage (fill cycles)
- n มาก → **Speedup ≈ จำนวน stage**

**5 stages ของ Load:** **Ifetch** → **Reg/Dec** → **Exec** (คำนวณ address) → **Mem** → **Wr** (write back)

**การวาด diagram:** แรเงาครึ่ง**ขวา** = **อ่าน** และแรเงาครึ่ง**ซ้าย** = **เขียน** (register file เขียนครึ่งแรกของ cycle และอ่านครึ่งหลัง)

**ตัวอย่างในสไลด์:** 100 คำสั่ง
- Single cycle 45 ns/cycle → 100 × 45 = **4500 ns**
- Multi-cycle 10 ns, CPI 4.6 → 100 × 4.6 × 10 = **4600 ns** (ช้ากว่า single cycle!)
- Ideal pipeline 10 ns, fill 4 cycles → (4 + 99) × 10 = **1030 ns** (ถ้านับแบบ Patterson คือ (100+4)×10 = 1040 ns)
- → **pipeline เร็วสุด** ประมาณ **4.4 เท่า** ของ single cycle

### 6.3 Hazards 3 ประเภท

| Hazard | สาเหตุ | ตัวอย่าง laundry | ใน processor |
|---|---|---|---|
| **Structural** | resource มีจำกัด มีคนต้องใช้พร้อมกัน | washer กับ dryer เป็นเครื่องเดียวกัน หรือ folder ไปดูทีวี | **memory เดียวใช้ทั้ง I-fetch และ data**, หรือ **2 คำสั่ง WB ใน cycle เดียวกัน** (register file มี write port เดียว) |
| **Data** | ต้องใช้ข้อมูลก่อนที่มันจะพร้อม ("ข้อมูลอยู่ในอนาคต") | เสื้อกับกางเกงชุดเดียวกันซักคนละรอบ | `LW $r2` แล้ว `ADD $r4,$r2,$r5` |
| **Control** | ยังไม่รู้ว่าคำสั่งถัดไปคืออะไร | ต้องดูผลซักก่อนจึงรู้ว่าใส่ผงซักฟอกเท่าไร | **branch** |

แก้แบบง่ายที่สุดคือ **รอ (stall)** แต่เสีย performance ดังนั้น pipeline control ต้อง **detect** แล้ว **resolve**

### 6.4 แก้ Structural Hazard
- **เพิ่ม resource** (แก้ด้วยเงิน) เช่น **แยก I-cache กับ D-cache**
- **Redesign:** กรณีคำสั่ง 3/4/5 cycles ปนกัน เช่น **LW (5 cycles) ตามด้วย ADD (4 cycles) จะ WB ใน cycle เดียวกัน**
  - (1) **stall** (ใส่ **bubble** ซึ่ง control ซับซ้อนและเสียโอกาส fetch: "no instruction is started in cycle 6")
  - (2) **ให้ R-type ใช้ 5 stages** (ใส่ MEM stage หลอก ๆ หรือ NOOP) → ไม่มี hazard แต่ R-type ช้าลง 1 cycle (**design trade-off**)
- **Exercise: ทำไม SW, BEQ, JMP ปนกับ R-type แล้วไม่เกิด structural hazard?** เพราะ **SW, BEQ และ JMP ไม่เขียน register file (ไม่มี WB)** จึงไม่แย่ง write port, SW ใช้ data memory ใน stage ของตัวเองเพียงคนเดียว และ BEQ/JMP แก้ PC ตั้งแต่ stage ต้น ๆ จึงไม่มี resource ไหนถูกใช้ซ้ำใน cycle เดียวกัน

### 6.5 แก้ Data Hazard
1. **Stall:** ADD รอ 3 cycles จน LW เขียน $r2 เสร็จ
2. **Forwarding / Bypassing:** ส่งผลจาก pipeline register (EX/MEM, MEM/WB) เข้า ALU ตรง ๆ ต้องเพิ่ม MUX
3. **Forwarding ไม่ได้ทุกกรณี "เว้นแต่มีไทม์แมชชีน":** **LW แล้วตามด้วยคำสั่งที่ใช้ค่านั้นทันที (load-use)** ข้อมูลเพิ่งได้ตอนจบ MEM ซึ่งช้ากว่าที่ EX ของคำสั่งถัดไปต้องใช้ → **ต้อง stall 1 cycle แม้จะมี forwarding**
4. **ให้ software ช่วย:** **reschedule** ย้ายคำสั่งอิสระมาแทรก (**delayed load**) ถ้าไม่มีให้แทรก **NOP**
   - ตัวอย่าง: `LW $r2,20($r1); NOP; NOP; NOP; AND $r4,$r2,$r5` (กรณีไม่มี forwarding)

### 6.6 แก้ Control Hazard
- ใน design นี้ branch รู้ผลใน cycle ที่ 3
- **Stall:** ช้าลง 2 cycles
- **Branch prediction:** ทาย taken/not taken ถ้าถูกไม่เสียเวลา ถ้าผิดเสียประมาณ 1 cycle
  - ทายมั่วยังถูกอย่างน้อย 50%
  - ใช้ branch history ได้ประมาณ 90%
- **Branch delay slot:** **คำสั่งที่อยู่หลัง branch ทำงานเสมอ** (branch มีผลช้าไป 1 cycle) ต้องให้ compiler หาคำสั่งที่ไม่เกี่ยวกับ branch มาใส่

```
ไม่มี delay slot:           มี delay slot:
ADD $r1,$r2,$r3            BEQ $r2,$r3,BRANCH
BEQ $r2,$r3,BRANCH         ADD $r1,$r2,$r3   ← ทำเสมอ (ย้ายมาจากข้างบน)
ORI $r4,$r5,#100           ORI $r4,$r5,#100
```
> ⚠️ ย้าย ADD มาไว้ใน slot ได้เพราะ BEQ **ไม่ได้ใช้ $r1** ถ้า BEQ ใช้ $r1 จะย้ายไม่ได้

## Part 2

### 6.7 Data Hazard 3 แบบ (i = คำสั่งหลัง, j = คำสั่งก่อน)

| ชนิด | เงื่อนไข | ความหมาย | ตัวอย่าง |
|---|---|---|---|
| **RAW** (Read After Write), true dependence | r ∈ **Rregs(i) ∩ Wregs(j)** | i อ่านก่อนที่ j จะเขียนเสร็จ | `a=7; b=a+5;` → **forwarding แก้ได้เกือบหมด** |
| **WAW** (Write After Write), output dependence | r ∈ **Wregs(i) ∩ Wregs(j)** | i เขียนเสร็จก่อน j ทำให้ค่าสุดท้ายผิด | `a=data[1000]; a=10; b=a+3;` (load ช้ากว่า) → แก้ด้วย design, software หรือ OoO + renaming |
| **WAR** (Write After Read), anti-dependence | r ∈ **Wregs(i) ∩ Rregs(j)** | i เขียนทับก่อนที่ j จะอ่าน | `a=sin(x); x=10;` (sin ต้องเตรียมนานจนอ่าน x ช้า) → **พบยากใน architecture สมัยใหม่** แก้ได้ด้วย design |

- **ทำไมไม่มี RAR?** เพราะการอ่านไม่เปลี่ยนค่า อ่านลำดับไหนก็ได้ผลเท่ากัน
- **ใน in-order 5-stage pipeline** (อ่านใน ID เขียนใน WB เสมอ) **มีแค่ RAW** ส่วน WAW/WAR เกิดเมื่อคำสั่งมี latency ต่างกัน หรือมี **out-of-order execution**

### 6.8 Pipelined Datapath
- ทุก stage มีคำสั่งคนละตัว ต้องมี **pipeline registers** ระหว่าง stage และต้อง**ส่ง control signals ตามไปด้วย** (Unified decoder: decode ครั้งเดียวที่ ID แล้วส่ง control ไปกับ pipeline)
- ตัวอย่าง "Give it a try" (address 10, 14, 20, 24 → beq ไป 100) แสดงว่า **ทุก cycle แต่ละ stage ทำคำสั่งต่างกัน** เช่น cycle 7: Fetch 100, Dcd 34, Ex 30, Mem 24, WB 20

**Hazard Detection** (เก็บ pending writes ไว้เทียบกับ operand ของคำสั่งปัจจุบัน):
```
hazard = ((rs==rw_ex)&regW_ex) | ((rs==rw_mem)&regW_mem) | ((rs==rw_wb)&regW_wb)
       | ((rt==rw_ex)&regW_ex) | ((rt==rw_mem)&regW_mem) | ((rt==rw_wb)&regW_wb)
```
**Forwarding circuit:** หา write ที่ใกล้ที่สุดซึ่งยัง valid แล้ว forward เข้า operand latch โดยเพิ่ม MUX จาก pipeline registers (**Data Forwarding = Data Bypassing**)

**Memory operations:** ถ้าคำสั่งเริ่ม in-order และ memory op อยู่ stage เดียวกันเสมอ **จะไม่มี hazard ระหว่าง memory ops** ส่วน load-use ใช้ "**Delayed loads**" (compiler scheduling)

### 6.9 Exercise: Rescheduling (forwarding เต็ม + delayed load + delayed branch)
```
เดิม:                        Reschedule:
Loop: LD   F0,0(R1)          Loop: LD   F0,0(R1)
      ADD  F4,F0,F2                LD   F1,8(R1)
      SD   0(R1),F4                ADD  F4,F0,F2
      LD   F1,8(R1)                ADD  F5,F1,F2
      ADD  F5,F1,F2                SD   0(R1),F4
      SD   8(R1),F5                SUB  R1,R1,#16
      SUB  R1,R1,#16               BNEZ R1,Loop
      BNEZ R1,Loop                 SD   -8(R1),F5   ← delay slot (offset ปรับเป็น 8−16 = −8 เพราะ R1 ลดไปแล้ว)
```
- ไม่มี load-use ติดกันแล้ว และ SUB ห่างจาก BNEZ พอ (ใช้ forwarding)
- **ประเด็นที่ทำให้ได้คะแนนเต็ม:** การชดเชย offset เมื่อย้าย SD ไปไว้หลัง SUB

---

# Chapter 7: Contemporary Architecture (ILP)

### 7.1 Flynn's Taxonomy (Michael Flynn, 1966)

| | Single Data | Multiple Data |
|---|---|---|
| **Single Instruction** | **SISD**: uniprocessor | **SIMD**: vector processor, GPU |
| **Multiple Instruction** | **MISD**: fault-tolerant computing | **MIMD**: multicore, distributed systems |

### 7.2 ILP = จำนวนคำสั่งที่ execute พร้อมกันได้
เทคนิค: **Vectorization**, **Speculative execution** (รวม branch prediction), **Pipelining/Superpipeline**, **Superscalar** (out-of-order execution, **register renaming**), **VLIW**

### 7.3 Vector Processor (SIMD)
- ทำ operation เดียวกับทั้ง vector (array)
- ตัวอย่าง: **Altivec** (Apple/Motorola/IBM), **Intel MMX, SSE, AVX**, GPU (CUDA, OpenCL)
- gcc `-O3` vectorize `C[i]=A[i]+B[i]` เป็น `paddd` (บวก 4 ints พร้อมกัน)
- เปรียบเทียบ: สั่ง "บะหมี่ 10 ถ้วย" ครั้งเดียว พ่อครัวรับ order ครั้งเดียวแล้วทำทั้งหมด

### 7.4 สูตร ILP และ CPU time (**ตารางนี้สำคัญมาก**)
k = จำนวน stage, n = จำนวนคำสั่ง, x = degree (issue width), m = จำนวน minor cycle ต่อ major cycle, T_c = major cycle

| Architecture | ILP (in flight) | T(n) | Speedup เมื่อ n ใหญ่ |
|---|---|---|---|
| **Pipeline** | k | (k + (n−1)) T_c | k (เทียบกับ non-pipeline) |
| **Superscalar** (degree x) | kx | (k + (n−x)/x) T_c | **x** (เทียบกับ pipeline) |
| **Superpipeline** (m minor cycles) | mk | (k + (n−1)/m) T_c | **m** |
| **Superpipelined superscalar** | mkx | (k + (n−x)/(mx)) T_c | mx |
| **VLIW** (x ops/word) | kx | (k + (n/x − x)) T_c *(ตามสไลด์)* | **x** |

- **Superscalar:** **hardware แจกคำสั่งแบบ dynamic** (เหมือนแถวซื้ออาหารแถวเดียว แล้ว manager แยกคนไปแถวข้าวกับแถวบะหมี่)
  - อาจเกิด **out-of-order completion** (คนสั่งบะหมี่ที่มาทีหลังได้ก่อน) → **WAR และ WAW** แก้ด้วย in-order completion หรือ register renaming
- **Superpipeline:** แบ่ง major cycle เป็น m minor cycles แล้วเริ่มคำสั่งใหม่ทุก minor cycle
- **VLIW:** **static scheduling** โดย compiler อัดหลาย operation ไว้ใน 1 คำสั่งยาว (เหมือนมี 2 แถวสั่งอาหารแยกตั้งแต่แรก แถวข้าวกับแถวบะหมี่)
- **SuperSymmetry: ที่ degree เท่ากัน superscalar, superpipeline และ VLIW ให้ performance เท่ากัน**

**Observations on VLIW:**
- **Software ของ Itanium กับ Itanium II ไม่ binary compatible** เพราะ static scheduling ผูก schedule กับจำนวนหน่วยหรือ latency ของ HW รุ่นนั้น พอเปลี่ยน HW ต้อง recompile
- Intel ประกาศ **EOL ของ Itanium ในเดือน ม.ค. 2019** และยังมี VLIW แบบอื่น เช่น **Transmeta Crusoe**

**Performance (Revisit) ตาราง IC/CPI/T_c** (L = latency ของคำสั่งแบบ single cycle):

| | IC | CPI | T_c | Speedup |
|---|---|---|---|---|
| Single cycle | n | 1 | L | 1 |
| Multi-cycle | n | 3–5 (avg 4.2) | L/5 | 1.xx |
| Pipeline | n | 1 | L/5 | 5 |
| Superscalar (degree k) | n | 1/k | L/5 | 5k |
| Superpipeline (m) | n | 1/m | L/5 | 5m |
| VLIW (x per word) | **n/x** | 1 | L/5 | 5x |

> ⚠️ **VLIW ลด IC** (หลาย op อยู่ใน 1 word) ส่วน **superscalar ลด CPI** นี่เป็นคำถาม concept ที่ชอบออก

**Speedup ด้วย pipeline 2 ชุด (Int + FP):** basic loop มีทั้งหมด 19 cycles โดย Int = 7 cycles และ FP = 12 (fmult 7 + fadd 5) → CPU time = max(Int, FP) → **speedup = 19/12 ≈ 1.6**

### 7.5 Compiler & ILP
- **Basic block เล็ก = มีโอกาสเติม slot น้อย** ต้องทำ basic block ให้ใหญ่ขึ้นด้วย **Loop Unrolling** หรือ **Software Pipelining**
- **Loop unroll** (`A[i] = A[i] + C`):
  - Loop ปกติใช้ **8 cycles/iteration** (มี stall หลัง LW 1 ครั้ง และหลัง ADD 2 ครั้ง)
  - Unroll 4 รอบ + reschedule + **register renaming** (ทำให้แต่ละ iteration ไม่แย่ง register กัน) ใช้ **14 cycles / 4 iterations = 3.5 cycles/iter** → **speedup = 8/3.5 ≈ 2.29**
  - Unroll 5 รอบ + superscalar (Int + FP) ใช้ **12 cycles / 5 iter = 2.4 cycles/iter** → speedup ≈ 3.33
  - **ข้อเสีย: code ใหญ่ขึ้น** และ**จำนวน register จำกัดจำนวนรอบที่ unroll ได้**
- **Software pipelining:** ในแต่ละรอบของ loop ใหม่ ทำงานคนละ stage ของคนละ iteration (เช่น SW ของ i, ADD ของ i+1, LW ของ i+2) มี **start-up** และ **clean-up** code → **performance ดีและ code ไม่ใหญ่มาก** (unroll เท่าที่จำเป็น)

### 7.6 Dynamic vs Static Scheduling

| **Dynamic** (Hardware, OoO) | **Static** (Software/Compiler) |
|---|---|
| HW unroll loop และ issue หลายคำสั่งแบบ dynamic | compiler unroll และ schedule หลายคำสั่งต่อ cycle (VLIW) |
| **Legacy software เร็วขึ้นบน HW ใหม่** | Compiler เห็น scope กว้างกว่า |
| HW ซับซ้อน ใช้ power สูงกว่า | HW ง่าย ใช้ power ต่ำ |
| | **Compatibility แย่** และ **dependency บางอย่างรู้ไม่ได้ตอน compile** (เช่น pointer alias หรือ cache miss) |

**สรุปจากสไลด์:** dynamic ทำให้ software เก่าได้ประโยชน์ ส่วน static จะดีกว่าถ้า compiler เก่งพอ แต่ **"proven to be too difficult to have good compiler"** → ในทางปฏิบัติ **dynamic (superscalar OoO) ชนะ**

### 7.7 Multicore & TLP
- Multicore = หลาย superscalar core ใน chip เดียว (multiple pipes)
- **Thread-Level Parallelism / SMT:** เมื่อ thread เดียวเติม slot ไม่เต็ม ก็ดึงคำสั่งจากหลาย thread มาใส่ pipeline พร้อมกัน → Intel เรียกว่า **Hyper-Threading**

### 7.8 Exercise: Dynamic Superscalar (degree 2, OoO)
มาจากตารางในสไลด์ (Issue / EX / MEM / WB):
- `LW f0` issue 1, EX 2, MEM 3, WB 4
- `ADD f2,f0,f1` issue 1 แต่ต้อง**รอ f0** จึง EX 5–7 (FP add 3 cycles) และ WB 8
- `SW f2` issue 2 และ**รอ f2** จึง MEM 9
- `SUB r1` issue 2, EX 4, WB 5 → **เสร็จก่อน ADD (out-of-order)**
- `BNE` issue 3, EX 6 → จากนั้น iteration ถัดไปเริ่ม issue ที่ cycle 4 ซ้อนกับรอบแรก

---

# Chapter 8: Memory Organization

## Part 1: Cache

### 8.1 Motivation
- ยุค 70s memory **เร็วกว่า** CPU (และ 640KB ก็พอ) ปัจจุบัน memory **ช้ามากเมื่อเทียบกับ** CPU (ขั้นต่ำ 4–8 GB)
- ปี 1980 CPU ไม่มี cache ส่วนปี 1995 มี cache 2 ระดับ
- **ตัวอย่าง:** memory op ใช้ 50 cycles, op อื่นใช้ 1 cycle และมี memory op 10% → เวลาที่รอ memory = (0.1×50)/(0.9×1 + 0.1×50) = 5/5.9 ≈ **85%**

**Design goal:** อยากได้ memory ที่ **large, fast, cheap** ใช้ **Hierarchy + Parallelism** (กฎทางกายภาพคือ large memory is slow)

**Hierarchy** (ใกล้ CPU = เร็ว เล็ก แพง): Registers → Cache → Main memory → Disk

| ระหว่าง | ใครจัดการ |
|---|---|
| Registers ↔ Memory | **Software** (compiler/programmer) |
| Cache ↔ Memory | **Hardware** |
| Memory ↔ Disk | **Hardware + OS** (virtual memory/paging) หรือ programmer (ผ่านไฟล์) |

### 8.2 Memory Technology

| | **DRAM** | **SRAM** |
|---|---|---|
| เทคโนโลยี | **Capacitor** | **Transistor** (flip-flop) |
| คุณสมบัติ | high density, low power, **cheap, slow**, **ต้อง refresh** | low density, high power, **expensive, fast**, ค่าอยู่ตลอดตราบที่มีไฟ |
| ใช้เป็น | **Main memory** | **Cache** |

- **Random access** = เวลาเข้าถึงคงที่ทุก location
- **Semi-random:** Disk, CD/DVD (มี seek + rotate)
- **Sequential:** tape (เวลาแปรตาม location แบบ linear)

### 8.3 Principle of Locality
ณ เวลาหนึ่ง software เข้าถึง address เพียงก้อนเล็ก ๆ
- **Temporal** ("tempo" = เวลา): เพิ่งใช้ก็จะใช้อีกเร็ว ๆ นี้ เช่น เพิ่งโทรหาใคร เบอร์นั้นควรอยู่บนสุดของ recent list หรือตัวแปรใน loop
- **Spatial** (space): ใช้ตัวนี้แล้วจะใช้ตัวข้าง ๆ เช่น ดึงเบอร์เพื่อนของเพื่อนมาพร้อมกัน, พกดินสอกับยางลบคู่กัน หรือ array

### 8.4 Terminology
- **Hit rate:** ความน่าจะเป็นที่เจอข้อมูลใน cache
- **Hit time:** เวลาเข้าถึง cache
- **Miss rate = 1 − hit rate**
- **Miss penalty:** เวลาดึงข้อมูลเข้า cache
- **Block (line):** หน่วยที่ย้ายเข้า/ออก cache ทีละทั้ง block

**4 คำถามของ memory hierarchy** (ใช้ได้กับ cache, TLB และ VM):
1. **Placement:** block วางที่ไหนได้
2. **Identification:** หา block เจอได้อย่างไร (tag)
3. **Replacement:** ตอน miss จะเอา block ไหนออก
4. **Write strategy:** เขียนแล้วเกิดอะไรขึ้น

### 8.5 Direct-Mapped Cache (เปรียบกับ: นักศึกษา 100 คนในหอประชุม = memory, เก้าอี้ 10 ตัวในห้องอาจารย์ = cache)

$$\boxed{\text{Index} = (\text{address} \bmod \text{cache size}) \ \text{div}\ \text{block size} \qquad \text{Tag} = \text{address div cache size}}$$

- ตัวอย่าง: cache size 10, block 1 → id 105 นั่ง index **5** (105 mod 10) และติด tag **10** (105 div 10)

**แบบ binary:** `| Tag | Index | Block offset | Byte offset |`
- offset bits = log₂(block size in bytes)
- index bits = log₂(#lines) = log₂(cache size / block size)
- tag bits = address bits − index − offset

**ตัวอย่างในสไลด์ 1:** address 32 bit, Tag [31:10], Index [9:2], Byte offset [1:0]
- **Block size = 4 bytes (1 word)**, จำนวน lines = 2⁸ = 256 → **cache size = 256 × 4 = 1 KB**
- **ตำแหน่งของ 0x00004098:** byte offset = 0, **index = (0x4098 >> 2) & 0xFF = 0x26 = 38**, **tag = 0x4098 >> 10 = 0x10 = 16**
- **Valid bit** = line นี้มีข้อมูลที่ใช้ได้ไหม (ตอนเปิดเครื่องเป็น 0)
- **Dirty bit** = ถูกเขียนแล้วแต่ยังไม่ได้เขียนกลับ memory (ใช้กับ write-back)

**ตัวอย่างในสไลด์ 2 (เพิ่ม spatial locality):** Tag [31:12], Index [11:4], Block offset [3:2], Byte offset [1:0]
- **Block = 4 words = 16 bytes**, 256 lines → **cache size = 4 KB**

### 8.6 Performance

$$\boxed{\text{Memory Access Time (AMAT)} = \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty}}$$
$$\boxed{CPI = CPI_{ideal} + (\text{Miss Rate} \times \text{Miss Penalty}) \ \ (\text{ต่อ memory access ต่อคำสั่ง})}$$

- Hit time และ miss penalty มักบอกเป็น **cycle**
- **Multilevel:** AMAT₀ = HitTime₀ + MissRate₀ × MissPenalty₀ โดย **MissPenalty₀ = AMAT₁** = HitTime₁ + MissRate₁ × MissPenalty₁
- ลด hit time ได้ด้วย **cache เล็ก** (สายสั้นลง และ comparator/MUX น้อยลง)

### 8.7 Sources of Miss (3C)

| Miss | สาเหตุ | วิธีแก้ |
|---|---|---|
| **Compulsory (Cold)** | เข้าถึงครั้งแรก cache ยังว่าง | ทำอะไรไม่ได้ (**prefetch** ช่วยได้), block ใหญ่ขึ้นช่วยลด |
| **Capacity** | cache เล็กเกินไปสำหรับ working set (กรณีสุดโต่งคือ **Ping-Pong effect**: cache มี 1 line ทุก address ใหม่จึง miss หมด เหมือนวางกระดาษบนโต๊ะได้ทีละแผ่น) | เพิ่ม cache size |
| **Conflict** | **cache ยังมีที่ว่าง แต่ mapping บังคับให้ชนกัน** | (1) เพิ่ม cache size (2) **associativity** (หลาย entry ต่อ index) |

### 8.8 Cache Configurations (5 อย่าง)
1. **Cache size**
2. **Block size**
   - ใหญ่ขึ้น = spatial locality ดีขึ้น (ลด compulsory miss)
   - แต่ **miss penalty สูงขึ้น** ("คนหลายคนเข้าห้องผ่านประตูเล็ก") เว้นแต่เพิ่มขนาด bus
   - ใหญ่เกินไปจะมีจำนวน block น้อยลง ทำให้ **temporal locality แย่ลงและ miss rate กลับเพิ่มขึ้น** (กราฟรูปตัว U ซึ่งต้อง benchmark เอง)
3. **Associativity**
   - **2-way:** 2 entries ต่อ index → conflict miss ลดลง
   - **4-way:** 4 comparators + MUX ใหญ่ → **hit time อาจสูงขึ้น**
   - **Fully associative:** ไม่มี index วางได้ทุกที่ → **conflict miss = 0** แต่ต้องมี **comparator เท่ากับจำนวน lines**
4. **Replacement:** **LRU** (ทิ้งตัวที่ไม่ได้ใช้นานที่สุด), **Round Robin**, FIFO, Random
   - **Direct mapped ไม่ต้องมี replacement algorithm** เพราะมีที่ให้วางได้ที่เดียว ต้องแทนที่ตัวเดิมเท่านั้น (Exercise)
   - ในทางปฏิบัติ **แยก I-cache กับ D-cache** (code มี spatial locality สูงกว่า)
5. **Write management**

### 8.9 Reducing Miss Penalty
ติดเก้าอี้ "ที่โถงทางเดิน" ระหว่างห้องอาจารย์กับหอประชุม = **L2 cache** → miss L1 อาจไป hit ที่ L2 ซึ่งใกล้กว่า memory มาก

### 8.10 Write Management

| | **Write Back** | **Write Through** |
|---|---|---|
| ทำอะไร | เขียนลง cache อย่างเดียว แล้วอัปเดต memory **ตอน replace** (ใช้ dirty bit) | เขียนทั้ง cache **และ** memory ทุกครั้ง |
| Repeated write | **ดี** | แย่ |
| ความเร็ว | เร็ว | ช้า |
| Multiprocessor | **ข้อมูล incoherent** | **ดีกว่า** (memory up-to-date เสมอ) |

- **Write allocate:** ตอน write miss ให้โหลด block เข้ามาก่อนแล้วจึงเขียน (= miss penalty + write time)
- **Write no-allocate:** เขียนตรงลงระดับล่างโดยไม่โหลด block
- สไลด์ใช้ **write through + write allocate** เพื่อความง่าย
- **Write buffer** (ใช้กับ write through): FIFO เล็ก ๆ (เช่น 4 words) ให้ CPU เขียนลง buffer แล้วทำงานต่อได้เลย ("มีคนวิ่งไปบอกที่หอประชุมแทน")
- **Write buffer saturation:** ถ้า memory ช้ากว่าอัตราการเขียนมาก buffer จะเต็ม**ไม่ว่าจะใหญ่แค่ไหน** → แก้ด้วย **L2 cache** (วิ่งไปแค่โถงทางเดิน)

### 8.11 Software & Cache
- Cache **transparent** ต่อ software แต่ programmer ยังใช้ประโยชน์เพิ่มได้
- **Row-major vs Column-major:** C เก็บ `int data[R][C]` แบบ **row-major** (data[0][0], data[0][1], …) ดังนั้น **วน `r` ข้างนอก `c` ข้างในเร็วกว่า** เพราะเข้าถึงแบบต่อเนื่อง (spatial) ส่วนการวน column ข้างนอกจะกระโดดทีละ 1 row ทำให้ miss บ่อย
- **ลด conflict miss:** array 3 ตัว `a[i], b[i], c[i]` มักตกที่ **cache index เดียวกัน** (ถ้าขนาด array ลงตัวกับขนาด cache) → แปลงเป็น **array of struct** `data[i].a/.b/.c` ให้อยู่ติดกันใน block เดียวกัน
- **Temporal:** ใช้ตัวแปรใน scope ซ้ำต่อเนื่องกัน

## Part 2: Virtual Memory

### 8.12 ทำไมต้องมี Virtual Memory (3 เหตุผล)
1. **Cost:** **รันซอฟต์แวร์ที่ต้องใช้ 4GB บนเครื่อง 2GB ได้** ด้วยการยืม secondary storage (demand loading/swap)
2. **Program relocatable:** แต่ละ process มี address space ของตัวเอง (0x100 ของ A ไม่ใช่ 0x100 ของ B)
3. **Protection (security):** A เข้าถึง memory ของ B โดยตรงไม่ได้

### 8.13 Paging

| Cache | Virtual memory |
|---|---|
| Block | **Page** (virtual) / **Page frame** (physical) |
| Miss | **Page fault** |
| จัดการโดย HW | **Fault จัดการโดย software (OS)** เพราะ HW ไม่รู้จัก file system หรือ swap |
| write back หรือ write through | **ใช้ write back เท่านั้น** (page out) เพราะ write through ไปดิสก์แพงเกินไป |

- Physical memory ทำหน้าที่เป็น **cache ของ disk** ใช้ **demand load** (โหลดตอน fault) และ replacement policy เป็นของ **OS**
- **Miss penalty มหาศาล** และ page ใหญ่ (เช่น **4KB**)
- **Page table** (**ต่อ process**) map VPN → PPN มี valid bit และ **access permission** (เช่น read-only) และมี **Page table register** ชี้ไปที่ตาราง

**ตัวอย่างในสไลด์:** VA 32 bit = **VPN 20 bit + offset 12 bit**, PA = **PPN 18 bit + offset 12 bit**
- **Page size** = 2¹² = **4 KB**
- **Physical memory** = 2³⁰ = **1 GB**
- **Page table size** = 2²⁰ entries × 4 bytes = **4 MB** (ต่อ process!)

### 8.14 TLB (Translation Lookaside Buffer)
- **Cache ของ page table entries ที่ใช้ล่าสุด** เข้าถึงเร็วพอ ๆ กับ cache (เร็วกว่า memory มาก)
- ขนาดเล็ก ไม่เกิน **128–256 entries** → ใช้ **fully associative** ได้ (เครื่องระดับกลางใช้ small n-way set associative)
- **TLB miss มีผลต่อ performance อย่างมีนัยสำคัญ**

### 8.15 Overlapped Cache & TLB Access
- ให้ลำดับปกติคือ VA → TLB → PA → cache ซึ่งช้า จึงทำ**ขนานกัน**: ใช้ **bits บนของ VA เปิด TLB** พร้อมกับใช้ **bits ล่าง (page offset ที่ไม่เปลี่ยนตอนแปล) เป็น cache index**
- **เงื่อนไข: index + offset ของ cache ต้องอยู่ใน page offset** หรือก็คือ **cache size / associativity ≤ page size**

Logic:
```
IF cache hit AND cache tag == PA  → ส่งข้อมูลให้ CPU
ELSE IF (cache miss OR tag != PA) AND TLB hit → เข้าถึง memory ด้วย PA จาก TLB
ELSE → ทำ VA translation ปกติ (เดิน page table)
```
- **กรณีทำไม่ได้:** cache 8KB direct-mapped กับ page 4KB → cache ใช้ **13 bits** แต่ page offset มี **12 bits** (bit 12 เปลี่ยนตอนแปล)
  - **ทางแก้:** (1) ใช้ **page 8KB** (2) ใช้ **2-way set associative** (เหลือ 4KB ต่อ way) (3) **ให้ SW รับประกันว่า VA[12] = PA[12]** (page coloring)
- **Exercise: page 4KB และ cache 32KB** → ต้องเป็น **8-way set associative** (32KB/8 = 4KB ต่อ way → index + offset = 12 bits พอดี)
- **Virtually addressed cache** (เข้า cache ด้วย VA ก่อนแปล) เร็ว แต่มีปัญหากับ **shared memory / aliasing** (VA ต่างกันจากต่าง process map ไป PA เดียวกัน) และตอน context switch
- **นอกขอบเขต:** overlay, segmentation, inverted page table, multilevel page table, virtualized page table

**Exercise: ตอน process switch**
- **TLB:** ต้อง **flush** (หรือติด **ASID/PID tag** ไว้ใน entry) เพราะ mapping ของ process เก่าไม่ถูกต้องสำหรับ process ใหม่
- **Page table:** **ไม่ต้องลบ** (เป็นของแต่ละ process) แค่เปลี่ยน **page table register** ให้ชี้ไปที่ table ของ process ใหม่
- **Cache:** ถ้าเป็น **physically addressed** **ไม่ต้อง flush** (PA ไม่กำกวม) แต่ถ้าเป็น **virtually addressed** ต้อง flush หรือใส่ PID tag

---

# Chapter 9: Storage Architecture

### 9.1 Storage & Interface Technology
- **SSD** (flash memory) vs **HDD** (mechanical disk)
- **Interfaces:** SAS (server, 12 Gb/s), SATA 3.0 (6 Gb/s), PCIe 3.0 x4 (31.5 Gb/s), Fibre Channel (128 Gb/s, server), USB (10 Gb/s), PATA (1064 Mb/s), parallel SCSI
- ⚠️ **Protocol/interface ≠ storage technology** (เช่น SSD อาจต่อผ่าน SATA หรือ PCIe ก็ได้)

### 9.2 Storage Virtualization
**นำเสนอ logical view ของ physical storage** มองสื่อทุกชนิดเป็น **single pool** = abstraction ที่ได้ logical storage หนึ่ง (หรือหลาย) ก้อนจาก physical หลายก้อน

### 9.3 RAID
- **R**edundant **A**rray of **I**ndependent (เดิมคือ **Inexpensive**) **D**isks
- คิดค้นโดย **Patterson, Gibson, Katz (UC Berkeley, 1987)**
- เป็น storage virtualization ที่ทำให้ **ดิสก์ราคาถูก (commodity) ได้ performance เทียบเท่าดิสก์แพง**
- แต่ละ level มีจุดสมดุลระหว่าง **reliability, availability, performance และ capacity** ต่างกัน

| Level | วิธี | Min disks | ทนเสีย | จุดเด่น/ด้อย |
|---|---|---|---|---|
| **RAID 0** | **Stripe** | **2** | **0** (เสีย 1 ลูกข้อมูลหายหมด) | performance สูง reliability ต่ำ |
| **RAID 1** | **Mirror** | **2** | 1 | ดีเมื่อ read และ reliability สำคัญ (capacity เหลือครึ่งเดียว) |
| RAID 2 | **Bit-level**, **Hamming code** | — | 1 | แทบไม่ใช้ |
| RAID 3 | **Byte-level** parity (dedicated) | 3 | 1 | ดีกับ long sequential read/write แย่กับ random |
| RAID 4 | **Block-level** parity บน**ดิสก์เฉพาะ** | 3 | 1 | read ดี **write ช้า (parity disk เป็น bottleneck)** |
| **RAID 5** | Block-level parity **กระจายทุกดิสก์** | **3** | 1 | **balance ระหว่าง performance กับ redundancy** |
| **RAID 6** | **2 parities** (block) | **4** | **2** | |

- **ทำไม RAID 5 เร็วกว่า RAID 4 (ตอนเขียน):** RAID 4 ต้องเขียน parity ลง**ดิสก์เดียว**ทุกครั้งที่มีการเขียน ดิสก์นั้นจึงเป็นคอขวด ส่วน RAID 5 **กระจาย parity ไปทุกดิสก์** ทำให้การเขียนหลายครั้งทำขนานกันได้ (และ read ก็ใช้ได้ครบทุกดิสก์)
- **Capacity:** RAID 0 = N, RAID 1 = N/2 (สำหรับ 2 ลูก), RAID 5 = N−1, RAID 6 = N−2 (หน่วยเป็นจำนวนดิสก์)
- **Nested RAID:** RAID 01 (mirror ของ stripes), **RAID 10** (stripe ของ mirrors), RAID 50
- **JBOD** (Just a Bunch Of Disks, **Span**): รวมดิสก์ที่**ขนาดต่างกัน**ได้ แต่**ไม่มี redundancy**

### 9.4 Network Storage: **Block vs File**

| | **SAN** (Storage Area Network) | **NAS** (Network Attached Storage) |
|---|---|---|
| ระดับ | **Block storage** (ผ่าน **iSCSI** ฯลฯ) | **File storage** ("network drive", map drive) |
| ใครจัดการ file system | **Client** (OS เห็นแค่ blocks/sectors) | **Host/server** (จัดการ FS และ permission ด้วย) |
| Sharing | **มักให้ระบบเดียวใช้ ไม่ share** | **share ระหว่าง clients ได้ง่าย** |
| HW | มักต้องมี HW เฉพาะหรือ fiber | ใช้ network ปกติ |
| Protocols | iSCSI (มี iATA/AoE แต่ไม่ค่อยนิยม) | **NFS, CIFS (SMB)**, AFP (deprecated), FTP/SFTP |

- **Object storage** (เช่น document) เป็นอีกประเภทหนึ่ง
- **Cloud:** **Amazon EBS = block**, **Amazon S3 = object**; **Google Persistent Disk = block**, **Google Cloud Filestore = file**
- **Exercise (cloud):** S3 = object, EBS = block, **DynamoDB = key-value/NoSQL database** (ไม่ใช่ block หรือ file), GCS bucket = object, Google Drive / OneDrive / Dropbox / iCloud = **file** (sync/share ไฟล์ ซึ่งภายในเก็บบน object storage)
- **Deduplication:** หลายระบบมีไฟล์หรือ block ซ้ำกัน ก็ใช้ร่วมกันเพื่อประหยัด physical space
- **Real-world considerations:** performance, price, block vs file vs object, sharing, reliability, redundancy, dedup

---

# Formula Sheet (หน้าเดียวจบ)

| เรื่อง | สูตร |
|---|---|
| Speedup / "X เร็วกว่า Y" | n = T_Y / T_X = Perf_X / Perf_Y |
| CPU time | IC × CPI × T_c = IC × CPI / f |
| Average CPI | Σ (CPI_i × freq_i) |
| MIPS | IC / (T × 10⁶) = f / (CPI × 10⁶) |
| Weighted AM | Σ w_i T_i |
| Geometric mean | (Π r_i)^(1/n), ใช้กับ ratio |
| Amdahl | 1 / ((1−P) + P/n), Max = 1/(1−P) |
| Single-cycle T_c | = critical path (LW: 230 ns ในตัวอย่าง) |
| Multi-cycle | cycles: LW 5, ORI/ORUI/ADD/SW 4, BEQ/JMP 3 |
| Pipeline | T = (k + n − 1) T_c, Speedup ≈ k |
| Superscalar (x) | T = (k + (n−x)/x) T_c |
| Superpipeline (m) | T = (k + (n−1)/m) T_c |
| Superpipelined superscalar | T = (k + (n−x)/(mx)) T_c |
| VLIW (x) | T = (k + (n/x − x)) T_c *(ตามสไลด์)*, IC → n/x |
| Cache index (decimal) | (addr mod cache size) div block size |
| Cache tag (decimal) | addr div cache size *(direct-mapped)* |
| Bits | offset = log₂(block B), index = log₂(#sets), tag = rest |
| #sets | cache size / (block size × ways) |
| AMAT | Hit time + Miss rate × Miss penalty |
| Multilevel | AMAT = H₁ + MR₁ × (H₂ + MR₂ × MP₂) |
| CPI with cache | CPI_ideal + Σ (accesses/instr × miss rate × penalty) |
| Page table size | 2^(VPN bits) × PTE size |
| Overlap condition | cache size / ways ≤ page size |
| RAID capacity | R0: N · R1: N/2 · R5: N−1 · R6: N−2 |

---

# ⚠️ กับดักที่ควรจำก่อนเข้าห้องสอบ

1. **Speedup = เวลาเก่า / เวลาใหม่** ห้ามกลับเศษกับส่วน
2. **Amdahl ใช้สัดส่วนของ "เวลา"** ถ้าโจทย์ให้สัดส่วนของ "จำนวนคำสั่ง" + CPI ให้คิดผ่าน CPI แทน
3. **Clock สูงกว่าไม่ได้แปลว่าเร็วกว่า** และ **MIPS สูงกว่าก็ไม่ได้แปลว่าเร็วกว่า** (IC ต่างกันตาม ISA)
4. **Multi-cycle ไม่ได้เร็วกว่า single-cycle เสมอ** (ตัวอย่างในสไลด์ 4600 vs 4500 ns)
5. **Pipeline ไม่ลด latency** แต่เพิ่ม throughput และ stage ที่ช้าที่สุดเป็นตัวกำหนด clock
6. **Load-use hazard แก้ด้วย forwarding อย่างเดียวไม่ได้** ต้องมี 1 stall หรือ reschedule
7. **ย้ายคำสั่งเข้า delay slot หรือ reschedule ต้องเช็ค dependency ก่อนเสมอ** ทั้ง RAW, WAR และ WAW
8. **WAR/WAW เกิดใน OoO หรือเมื่อคำสั่งมี latency ต่างกัน** ส่วน in-order 5-stage ปกติมีแค่ RAW
9. **VLIW ลด IC** ส่วน **superscalar ลด CPI** และ **dynamic scheduling ช่วยให้ legacy code เร็วขึ้น**
10. **Fully associative ไม่มี conflict miss** แต่ยังมี compulsory และ capacity miss
11. **Block ใหญ่ขึ้นไม่ได้ดีเสมอ** เพราะ miss penalty สูงขึ้นและจำนวน block ลดลง
12. **Direct mapped ไม่ต้องมี replacement policy**
13. **Write back + multiprocessor = ข้อมูล incoherent** ส่วน write through เหมาะกับ multiprocessor กว่า
14. **VM ใช้ write back เท่านั้น** และ **page fault จัดการด้วย OS (software)**
15. **Page table เป็นของแต่ละ process** ตอน context switch ให้ flush **TLB** ไม่ใช่ลบ page table
16. **RAID ไม่ใช่ backup** และ **RAID 0 ไม่มี redundancy**
17. **SAN = block (client จัดการ FS)** ส่วน **NAS = file (server จัดการ FS)**
18. **Little endian = LSB อยู่ address ต่ำ** (Intel) และ **big endian = MSB อยู่ address ต่ำ**
