*<div align="right"> Vikram Procter, Minh Do | Dec, 2025 </div>*

# Relay Machine - 4-bit Computer Made of Relays

## Project Overview

This project implements a very simple 4-bit computer architecture 

## Systems Overview
-   ALU (computes numbers)
-   Program Memory (the program with program counter)
-   Registers
-   Display


## Relays
Using a 24V 0.15W relay [J104D2C24VDC.15S](https://www.digikey.ca/en/products/detail/cit-relay-and-switch/J104D2C24VDC-15S/12502730)


## Gate Implementations with Relay
![NOT Gate](./pics/NOT_A'.jpg)
*AND Gate Y=A'*

![AND Gate](./pics/AND_AB_AB'.jpg)
*AND Gate Y1=AB and Y2=AB'*

![OR Gate](./pics/OR_A+B_A+B'.jpg)
*OR Gate Y1=A+B and Y2=A+B'*

![XOR Gate](./pics/XOR_XNOR_AxB_(AxB)'.jpg)
*XOR and XNOR Gate Y1=AxB and Y2=(AxB)'*

![XOR AND Gate](./pics/XOR_AND_C(AxB).jpg)
*XOR AND and XNOR AND Gate Y1=C(AxB) and Y2=C(AxB)'*



## OP-Codes
### ALU Operations:
- ADD  (addition)
- SUB  (subtraction)
- AND  (bitwise AND)
- OR   (bitwise OR)
- XOR  (bitwise exclusive OR)
- LS   (Logic shift both ways)

### Registry Operations:
- LDI  (Load immediate)
- MOV  (Move data from reg to reg)

### Program Counter Operations
- BRGE (branch if greater or equal)
- BREQ (branch if equal)
- JMP  (jump program counter)

### Miscellaneous Operations
- NOP  (No Operation)


| OpCode [3:0]   | Top [3:0]  | Bottom [3:0]  | Description       |
| -------------- | ---------- | ------------- | ----------------- |
| 0000           | 0000       | 0000          | NOP: No Operation |
| 0001           | dddd       | rrrr          | ADD: Rd ← Rd + Rr |
| 0010           | dddd       | rrrr          | AND: Rd ← Rd & Rr |
| 0011           | dddd       | rrrr          | OR:  Rd ← Rd o Rr |
| 0100           | 0000       | 0000          | 
| 0101           | dddd       | rrrr          | SUB: Rd ← Rd - Rr |
| 0110           | dddd       | rrrr          | XOR: Rd ← Rd x Rr |
| 0111           | 0000       | 0000          | LS:  Rd ← Rd x Rr
| 1000           | kkkk       | kkkk          | JMP: PC ← PC + k + 1 |
| 1001           | dddd       | kkkk          | LDI: Rd ← K
| 1010           | 0000       | 0000          |
| 1011           | dddd       | rrrr          | MOV: Rd ← Rr
| 1100           | kkkk       | kkkk          | BRGE: PC ← PC + k + 1 |
| 1101           | kkkk       | kkkk          | BREQ: PC ← PC + k + 1 |
| 1110           | 0000       | 0000          |
| 1111           | 0000       | 0000          |




