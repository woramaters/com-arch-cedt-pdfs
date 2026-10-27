# Formula Sheet

| เรื่อง | สูตร |
|---|---|
| Performance | Performance = 1 / Execution time |
| Speedup ("X เร็วกว่า Y n เท่า") | n = T<sub>Y</sub> / T<sub>X</sub> = T<sub>old</sub> / T<sub>new</sub> |
| CPU time | **IC × CPI × T<sub>c</sub> = IC × CPI / f** |
| Cycle time | T<sub>c</sub> = 1 / f (1 GHz → 1 ns) |
| Average CPI | Σ(CPI<sub>i</sub> × freq<sub>i</sub>) |
| MIPS | IC / (T × 10⁶) = f / (CPI × 10⁶) |
| Weighted AM | Σ w<sub>i</sub>T<sub>i</sub> |
| Geometric mean | (Π r<sub>i</sub>)^(1/n) ใช้กับ ratio |
| **Amdahl** | **1 / ((1 − P) + P/n)** โดย P = สัดส่วน**เวลา** |
| Amdahl max | 1 / (1 − P) |
| Single cycle | T<sub>c</sub> = critical path (LW = 230 ns ในสไลด์) และ CPI = 1 |
| Multi-cycle (nanoLADA) | **LW 5 · ORI/ORUI/ADD/SW 4 · BEQ/JMP 3** |
| Pipeline (k stages) | T = (k + n − 1) T<sub>c</sub> และ speedup → k |
| Laundry k loads (4 ขั้น × 30 นาที) | (k + 3) / 2 ชั่วโมง |
| Superscalar (x) | T = (k + (n − x)/x) T<sub>c</sub> |
| Superpipeline (m) | T = (k + (n − 1)/m) T<sub>c</sub> |
| Superpipelined superscalar | T = (k + (n − x)/(m·x)) T<sub>c</sub> |
| VLIW (x) | T = (k + (n/x − x)) T<sub>c</sub> (ตามสไลด์) และ IC → n/x |
| Cache index (ฐานสิบ) | (addr mod cache size) div block size |
| Cache tag (ฐานสิบ, direct) | addr div cache size |
| Cache bits | offset = log₂(block B), index = log₂(#sets), tag = ที่เหลือ |
| จำนวน sets | cache size / (block size × ways) |
| AMAT | Hit time + Miss rate × Miss penalty |
| AMAT 2 ระดับ | H₁ + MR₁ × (H₂ + MR₂ × MP₂) |
| CPI with cache | CPI<sub>ideal</sub> + Σ(accesses/instr × miss rate × penalty) |
| Page table size | 2^(VPN bits) × PTE size |
| Overlap condition | cache size / ways ≤ page size |
| RAID capacity | R0: N · R1: N/2 · R5: N − 1 · R6: N − 2 |
| 2's complement range | −2ⁿ⁻¹ … 2ⁿ⁻¹ − 1 |
| Unsigned range | 0 … 2ⁿ − 1 |
| Full adder | S = A ⊕ B ⊕ Cin และ Cout = AB + Cin(A ⊕ B) |
| FF ขั้นต่ำของ FSM | ⌈log₂(#states)⌉ |
| MUX 2ⁿ-to-1 | มี n select lines |

# กับดักรวม (อ่านก่อนเข้าห้องสอบ)

::: trap
**Performance & ISA**
1. **Speedup = เวลาเก่า / เวลาใหม่** ห้ามกลับเศษกับส่วน
2. **Amdahl ใช้สัดส่วนของ "เวลา"** ถ้าโจทย์ให้สัดส่วนของ "จำนวนคำสั่ง" + CPI ให้คิดผ่าน CPI แทน
3. **Clock สูงกว่าไม่ได้แปลว่าเร็วกว่า** และ **MIPS สูงกว่าไม่ได้แปลว่าเร็วกว่า** (IC ต่างกันตาม ISA)
4. **GM ทำนายเวลาจริงไม่ได้** แต่ consistent ไม่ว่าจะใช้อะไรเป็น baseline
5. **Little endian = LSB อยู่ address ต่ำ** (Intel) และ **big endian = MSB อยู่ address ต่ำ**
6. **Vector table เก็บ address** (ต้องอ่าน memory อีกครั้ง) ส่วน **handler table เก็บโค้ด** (กระโดดไปได้เลย)
:::

::: trap
**Processor & Pipeline**
7. **Multi-cycle ไม่ได้เร็วกว่า single cycle เสมอ** (สไลด์: 4600 vs 4500 ns)
8. **Pipeline ไม่ลด latency** แต่เพิ่ม throughput และ **stage ที่ช้าที่สุด**กำหนด clock
9. **Load-use แก้ด้วย forwarding อย่างเดียวไม่ได้** ต้อง stall 1 cycle หรือ reschedule
10. **ก่อนย้ายคำสั่งเข้า delay slot หรือ reschedule ต้องเช็ค RAW/WAR/WAW**
11. **In-order 5-stage มีแค่ RAW ที่เป็นปัญหาจริง** ส่วน WAR/WAW มาพร้อม OoO หรือ latency ที่ต่างกัน
12. **VLIW ลด IC** ส่วน **superscalar ลด CPI** และ **dynamic scheduling ทำให้ legacy code เร็วขึ้น**
:::

::: trap
**Memory & Storage**
13. **Fully associative ไม่มี conflict miss** แต่ยังมี compulsory และ capacity miss
14. **Block ใหญ่ขึ้นไม่ได้ดีเสมอ** (miss penalty สูงขึ้น และถ้าใหญ่เกินไป miss rate กลับเพิ่ม)
15. **Direct-mapped ไม่ต้องมี replacement policy**
16. **Write-back + multiprocessor = incoherent** ส่วน write-through เหมาะกับ multiprocessor กว่า
17. **VM ใช้ write-back เท่านั้น** และ **page fault จัดการโดย OS**
18. **Page table มีต่อ process** ตอน context switch ต้อง flush **TLB** ไม่ใช่ลบ page table
19. **RAID ไม่ใช่ backup** และ **RAID 0 ไม่ทนเสีย**
20. **SAN = block (client จัดการ FS)** ส่วน **NAS = file (server จัดการ FS)**
:::

# Glossary A–Z (ค้นหาเร็ว)

| คำ | ย่อมาจาก / ชื่อเต็ม | ความหมายสั้น ๆ | บท |
|------------|----------------|------------------------------------|---|
| ABI | Application Binary Interface | ข้อตกลงระดับ binary: calling convention, stack frame, alignment | 1, 3 |
| Accumulator | — | ISA แบบ 1-address มี register หลักตัวเดียวเป็น implicit operand | 3 |
| Addressing mode | — | วิธีระบุตำแหน่ง operand (immediate, displacement, indirect, ...) | 3 |
| Alignment | — | ข้อมูลขนาด s ต้องเริ่มที่ address ที่ mod s = 0 (restricted) | 3 |
| ALU | Arithmetic Logic Unit | วงจรคำนวณ +, −, AND, OR ตาม alu_ops และมี zero flag | 0, 4 |
| AMAT | Average Memory Access Time | Hit time + Miss rate × Miss penalty | 8 |
| Amdahl's Law | — | speedup รวมถูกจำกัดด้วยส่วนที่ไม่ได้เร่ง | 2 |
| Associativity | — | จำนวน way ต่อ set ของ cache (direct = 1 way) | 8 |
| Basic block | — | ลำดับคำสั่งที่ไม่มี branch เข้า/ออกตรงกลาง | 3, 7 |
| BCD | Binary-Coded Decimal | ใช้ 4 bits ต่อเลขฐานสิบ 1 หลัก | 0 |
| Benchmark | — | ชุดโปรแกรมมาตรฐานสำหรับวัด performance | 2 |
| Big endian | — | MSB อยู่ address ต่ำ (PowerPC, Sun) | 3 |
| Block (cache line) | — | หน่วยข้อมูลที่ย้ายเข้าออก cache ทั้งก้อน | 8 |
| Branch delay slot | — | คำสั่งถัดจาก branch ที่ทำงานเสมอ | 6 |
| Branch prediction | — | ทาย taken/not taken ล่วงหน้า (history ถูกประมาณ 90%) | 6, 7 |
| Bubble | — | ช่องว่างใน pipeline ที่เกิดจาก stall | 6 |
| Bus | — | ชุดสายสัญญาณที่ใช้ร่วมกันส่ง data/address/control | 1 |
| Cache | — | SRAM เล็กและเร็ว เก็บสำเนาข้อมูลที่ใช้บ่อย จัดการโดย HW | 8 |
| Callee/Caller save | — | ใครเป็นคน save register ตอนเรียก subroutine | 3 |
| Capacity miss | — | miss เพราะ cache เล็กกว่า working set | 8 |
| CIFS / SMB | Common Internet File System / Server Message Block | protocol แชร์ไฟล์ของ Windows (NAS) | 9 |
| CISC | Complex Instruction Set Computer | คำสั่งซับซ้อน ความยาวแปรผัน (x86, VAX) | 3 |
| CLA | Carry-Lookahead Adder | adder ที่คำนวณ carry ขนานด้วย generate/propagate | 0 |
| Clock rate | — | จำนวน cycle ต่อวินาที (Hz) | 0, 2 |
| Code motion | — | ย้ายโค้ด loop-invariant ออกนอก loop | 3 |
| Compulsory (cold) miss | — | miss ตอนเข้าถึง block ครั้งแรก | 8 |
| Conflict miss | — | miss เพราะ mapping ชนกัน ทั้งที่ cache ยังว่าง | 8 |
| Control hazard | — | ไม่รู้คำสั่งถัดไปเพราะ branch | 6 |
| Control unit | — | decode opcode แล้วสร้าง control signals | 4, 5 |
| Copy propagation | — | แทนตัวแปรที่ถูก copy ด้วยต้นฉบับ | 3 |
| CPI | Clock (cycles) Per Instruction | จำนวน cycle เฉลี่ยต่อคำสั่ง | 2 |
| CPU time | — | IC × CPI × T<sub>c</sub> | 2 |
| Critical path | — | path ที่ delay มากที่สุด กำหนด cycle time | 0, 4 |
| CSE | Common Subexpression Elimination | คำนวณนิพจน์ซ้ำเพียงครั้งเดียว | 3 |
| Data hazard | — | ใช้ข้อมูลก่อนที่มันจะพร้อม (RAW/WAR/WAW) | 6 |
| Datapath | — | ส่วนที่เก็บ ย้าย และประมวลผลข้อมูล | 4 |
| Decoder | — | n bits → เลือก output 1 จาก 2ⁿ เส้น (one-hot) | 0 |
| Deduplication | — | เก็บข้อมูลซ้ำไว้ชุดเดียว | 9 |
| Direct-mapped | — | แต่ละ block วางได้ที่เดียวใน cache | 8 |
| Dirty bit | — | block ถูกแก้แต่ยังไม่เขียนกลับ (write-back) | 8 |
| Displacement | — | addressing แบบ M[R + const] เช่น G.age | 3 |
| DRAM | Dynamic RAM | capacitor, ถูก, หนาแน่น, ช้า, ต้อง refresh → main memory | 8 |
| Dynamic scheduling | — | HW จัดลำดับคำสั่งตอนรัน (OoO superscalar) | 7 |
| EBS | (Amazon) Elastic Block Store | cloud block storage | 9 |
| Endian | — | ลำดับ byte ของข้อมูลหลาย byte ใน memory | 3 |
| EPC | Exception Program Counter | register เก็บ PC ที่จะกลับไปหลัง exception | 5 |
| Exception | — | unprogrammed control flow (interrupt/trap) | 3 |
| Extender | — | ขยาย imm 16 → 32 bits (sign/zero extend, zero pad) | 4 |
| Fetch | — | IR ← MEM[PC]; PC ← PC + 4 | 4, 5 |
| FLOPS | Floating-Point Operations Per Second | หน่วยวัดการคำนวณทศนิยม (เชิงการตลาด) | 2 |
| Flip-flop | — | หน่วยจำ 1 บิตที่เปลี่ยนค่าที่ขอบ clock | 0 |
| Flynn's taxonomy | — | SISD, SIMD, MISD, MIMD | 7 |
| Forwarding / Bypassing | — | ส่งผลจาก pipeline register ตรงเข้า ALU | 6 |
| FSM | Finite State Machine | วงจร sequential ที่มี state จำกัด และเป็น control ของ multi-cycle | 0, 5 |
| Fully associative | — | block วางที่ใดก็ได้ ไม่มี conflict miss | 8 |
| Geometric mean | — | ค่าเฉลี่ยของ ratio ที่ consistent กับทุก baseline | 2 |
| Gray code | — | รหัสที่ค่าติดกันต่างกัน 1 บิต (แกน K-map) | 0 |
| Handler table | — | ตารางที่เก็บโค้ด handler ขนาดคงที่ | 3 |
| Hazard | — | เหตุที่ pipeline เดินตามจังหวะปกติไม่ได้ | 6 |
| Hit / Miss rate | — | สัดส่วนที่หาเจอหรือไม่เจอใน cache (miss = 1 − hit) | 8 |
| Hyper-Threading | — | ชื่อ SMT ของ Intel | 1, 7 |
| IC | Instruction Count | จำนวนคำสั่งที่รันจริง | 2 |
| ILP | Instruction-Level Parallelism | จำนวนคำสั่งที่ทำพร้อมกันได้ | 7 |
| Immediate | — | ค่าคงที่ที่ฝังในคำสั่ง (#10) | 3 |
| Index | — | บิตของ address ที่ใช้เลือก set/line ของ cache | 8 |
| Interrupt | — | exception จาก hardware ภายนอก | 3 |
| IR | Instruction Register | register เก็บคำสั่งที่ fetch มา (multi-cycle) | 5 |
| ISA | Instruction Set Architecture | interface ระหว่าง SW กับ HW | 1, 3 |
| iSCSI | Internet SCSI | ส่งคำสั่ง block ผ่าน IP (ใช้ทำ SAN) | 9 |
| JBOD | Just a Bunch Of Disks | span ดิสก์ต่างขนาด ไม่มี redundancy | 9 |
| K-map | Karnaugh map | ตารางช่วยลดรูป Boolean (Gray code, wrap around) | 0 |
| Latency | — | เวลาของงานเดี่ยวตั้งแต่เริ่มจนเสร็จ | 2, 6 |
| Little endian | — | LSB อยู่ address ต่ำ (Intel) | 3 |
| Load-store | — | ISA ที่เข้าถึง memory ผ่าน LD/ST เท่านั้น (RISC) | 3 |
| Load-use hazard | — | ใช้ค่าจาก LW ทันที ต้อง stall 1 cycle แม้มี forwarding | 6 |
| Locality | — | temporal (เวลา) และ spatial (พื้นที่) | 8 |
| Loop unrolling | — | คลี่ loop ให้ basic block ใหญ่ขึ้น | 7 |
| LRU | Least Recently Used | ทิ้ง block ที่ไม่ได้ใช้นานที่สุด | 8 |
| Mealy / Moore | — | output ขึ้นกับ state + input / state อย่างเดียว | 0 |
| Microprogram | — | control แบบเก็บ microinstruction ใน ROM | 5 |
| MIMD / MISD | Multiple Instruction Multiple / Single Data | multicore / fault-tolerant | 7 |
| MIPS (หน่วย) | Millions of Instructions Per Second | หน่วยเชิงการตลาด เทียบข้าม ISA ไม่ได้ | 2 |
| Miss penalty | — | เวลานำ block เข้า cache เมื่อ miss | 8 |
| Moore's Law | — | transistor เพิ่ม 2 เท่าทุก ~2 ปี (ข้อสังเกต) | 1 |
| MSB / LSB | Most / Least Significant Bit | บิตซ้ายสุด / ขวาสุด | 0 |
| MUX | Multiplexer | เลือก 1 จาก 2ⁿ อินพุตด้วย n select bits | 0, 4 |
| nanoLADA | — | RISC ISA ที่ใช้สอนในวิชา (7 คำสั่ง, 3 formats) | 4 |
| NAS | Network Attached Storage | file storage ผ่าน network (NFS, SMB) | 9 |
| NFS | Network File System | protocol แชร์ไฟล์ (Unix) | 9 |
| NOP | No OPeration | คำสั่งที่ไม่ทำอะไร ใช้เว้นระยะ | 6 |
| Object storage | — | เก็บเป็น object ผ่าน API (S3) | 9 |
| Offset | — | บิตล่างของ address ที่เลือก byte ใน block/page | 8 |
| OoO | Out-of-Order execution | ทำคำสั่งที่ operand พร้อมก่อน | 7 |
| Opcode | Operation code | field บอกชนิดคำสั่ง (6 bits ใน nanoLADA) | 3, 4 |
| Organization | Computer Organization | โครงสร้างภายในที่ implement ISA | 1 |
| Overflow | — | ผลเกินช่วง signed (บวก + บวก ได้ลบ) | 0 |
| Page / Page frame | — | block ของ VM ฝั่ง virtual / physical | 8 |
| Page fault | — | miss ของ VM ที่ OS จัดการ | 8 |
| Page table | — | ตาราง VPN → PPN ต่อ process | 8 |
| Parity | — | ข้อมูล XOR สำหรับกู้ดิสก์ที่เสีย | 9 |
| PC | Program Counter | register เก็บ address ของคำสั่งถัดไป | 3, 4 |
| PC-relative | — | branch target = PC + displacement (relocatable) | 3 |
| Pipeline | — | ทำหลายคำสั่งซ้อนกันคนละ stage | 6 |
| PLA / PAL | Programmable Logic Array / Array Logic | AND–OR plane ที่ program ได้ ใช้ทำ control | 0, 4 |
| RAID | Redundant Array of Independent Disks | รวมดิสก์เพื่อ performance/redundancy | 9 |
| RAM | Random Access Memory | เวลาเข้าถึงคงที่ทุกตำแหน่ง | 8 |
| RAW / WAR / WAW | Read After Write / Write After Read / Write After Write | ชนิดของ data hazard | 6 |
| Register file | — | 32 × 32-bit, อ่าน 2 port, เขียน 1 port | 4 |
| Register renaming | — | ใช้ physical register ต่างกันเพื่อลบ WAR/WAW | 7 |
| Response time | — | เวลาของงานหนึ่งงาน (= latency) | 2 |
| RISC | Reduced Instruction Set Computer | คำสั่งพื้นฐาน, fixed length, load-store | 3 |
| ROM | Read-Only Memory | เก็บ truth table หรือ microprogram | 0, 5 |
| RTL | Register Transfer Language | สัญกรณ์อธิบายการย้ายข้อมูลของคำสั่ง | 4, 5 |
| S3 | (Amazon) Simple Storage Service | cloud object storage | 9 |
| SAN | Storage Area Network | block storage ผ่าน network (iSCSI) | 9 |
| SAS / SATA | Serial Attached SCSI / Serial ATA | interface ของ storage | 9 |
| Set-associative | — | block วางได้ใน n ways ของ set ตัวเอง | 8 |
| Sign extension | — | ขยายบิตโดยคัดลอก sign bit | 0, 4 |
| SIMD / SISD | Single Instruction Multiple / Single Data | vector processor / uniprocessor | 7 |
| SMT | Simultaneous MultiThreading | ดึงคำสั่งจากหลาย thread เข้า pipeline | 7 |
| Software pipelining | — | จัด loop ให้ทำคนละขั้นของคนละ iteration | 7 |
| SPEC | Standard Performance Evaluation Corporation | องค์กร benchmark มาตรฐาน | 2 |
| Speculative execution | — | ทำงานล่วงหน้าก่อนรู้แน่ว่าต้องทำ | 7 |
| Speedup | — | T<sub>old</sub> / T<sub>new</sub> | 2 |
| SRAM | Static RAM | transistor, เร็ว, แพง, ไม่ต้อง refresh → cache | 8 |
| SSD / HDD | Solid State / Hard Disk Drive | flash / จานแม่เหล็ก | 9 |
| Stack architecture | — | ISA แบบ 0-address ใช้ top of stack | 3 |
| Stall | — | หยุดคำสั่งใน pipeline รอ | 6 |
| Static scheduling | — | compiler จัดลำดับคำสั่ง (VLIW) | 7 |
| Strength reduction | — | ใช้ operation ที่ถูกกว่า เช่น shift แทนคูณ | 3 |
| Striping / Mirroring | — | กระจายข้อมูล / ทำสำเนา (RAID 0 / RAID 1) | 9 |
| Structural hazard | — | resource ไม่พอ ถูกแย่งใช้พร้อมกัน | 6 |
| Superpipeline | — | แบ่ง cycle เป็น m minor cycles | 7 |
| Superscalar | — | หลาย pipeline, HW issue หลายคำสั่งต่อ cycle | 7 |
| Tag | — | บิตบนของ address เก็บใน cache ไว้ตรวจ hit | 8 |
| Throughput | — | จำนวนงานที่เสร็จต่อหน่วยเวลา | 2, 6 |
| TLB | Translation Lookaside Buffer | cache ของ page table entries | 8 |
| TLP | Thread-Level Parallelism | ความขนานระดับ thread | 7 |
| Trap | — | exception จาก software | 3 |
| 2's complement | Two's complement | −X = กลับบิต + 1 | 0 |
| Valid bit | — | line นี้มีข้อมูลที่ใช้ได้หรือยัง | 8 |
| Vector table | — | ตารางที่เก็บ address ของ handler | 3 |
| Virtual memory | — | address space เสมือนต่อ process (cost, relocation, protection) | 8 |
| VLIW | Very Long Instruction Word | compiler รวมหลาย op ใน 1 คำสั่ง (static) | 7 |
| VPN / PPN | Virtual / Physical Page Number | ส่วนบนของ VA / PA | 8 |
| Write allocate | — | write miss แล้วโหลด block มาก่อนเขียน | 8 |
| Write-back / Write-through | — | เขียน cache แล้วค่อยเขียนกลับ / เขียนทั้งสองที่ทันที | 8 |
| Write buffer | — | FIFO พักการเขียนของ write-through | 8 |
| XOR | Exclusive OR | เป็น 1 เมื่ออินพุตต่างกัน | 0, 3 |
