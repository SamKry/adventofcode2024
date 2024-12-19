import numpy as np
import array
from pprint import pprint

dataFile = "python/17/data.txt"
# dataFile = "python/17/data_small.txt"

""""
example:

Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


with open(dataFile) as f:
    A = int(f.readline().split(":")[1])
    B = int(f.readline().split(":")[1])
    C = int(f.readline().split(":")[1])
    # empty line
    f.readline()

    data = f.readline().split(":")[1].strip()
    programm = [int(x) for x in data.split(",")]

pointer = 0


def func(arg):
    pass


"""
There are two types of operands; each instruction specifies the type of its operand. The value of a literal operand is the operand itself. For example, the value of the literal operand 7 is the number 7. The value of a combo operand can be found as follows:

Combo operands 0 through 3 represent literal values 0 through 3.
Combo operand 4 represents the value of register A.
Combo operand 5 represents the value of register B.
Combo operand 6 represents the value of register C.
Combo operand 7 is reserved and will not appear in valid programs.
The eight instructions are as follows:

The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.

The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.

The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.

The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.

The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)

The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)

The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)

The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
"""

def getComboOperand(operand):
    if operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    elif operand == 7:
        print("Error: Operand 7 is reserved and will not appear in valid programs.")
        exit(1)
    else:
        return operand

ans = []


print("A: ", A)
print("B: ", B)
print("C: ", C)
print("Program: ", programm)
print("Pointer: ", pointer)
print("=====================================")

while True:
    if pointer >= len(programm ) - 1:
        print("Program finished")
        break
    instruction = programm[pointer]

    if instruction == 0:
        print("adiv with: ", A, " and ", getComboOperand(programm[pointer + 1]))
        A = A // (2 ** getComboOperand(programm[pointer + 1]))
        pointer += 2
    elif instruction == 1:
        print("bxl with: ", B, " and ", programm[pointer + 1])
        B = B ^ programm[pointer + 1]
        pointer += 2
    elif instruction == 2:
        print("bst with: ", getComboOperand(programm[pointer + 1]))
        B = getComboOperand(programm[pointer + 1]) % 8
        pointer += 2
    elif instruction == 3:
        print("jnz with: ", A, " and ", programm[pointer + 1])
        if A != 0:
            pointer = programm[pointer + 1]
        else:
            print("\tA is 0")
            pointer += 2
    elif instruction == 4:
        print("bxc with: ", B, " and ", C)
        B = B ^ C
        pointer += 2
    elif instruction == 5:
        print("out with: ", getComboOperand(programm[pointer + 1]))
        ans.append(getComboOperand(programm[pointer + 1]) % 8)
        print("Temp Answer: ", ans)
        pointer += 2
    elif instruction == 6:
        print("bdv with: ", A, " and ", getComboOperand(programm[pointer + 1]))
        B = A // (2 ** getComboOperand(programm[pointer + 1]))
        pointer += 2
    elif instruction == 7:
        print("cdv with: ", A, " and ", getComboOperand(programm[pointer + 1]))
        C = A // (2 ** getComboOperand(programm[pointer + 1]))
        pointer += 2

    print("Instruction: ", instruction)
    print("A: ", A)
    print("B: ", B)
    print("C: ", C)
    print("Pointer: ", pointer)
    print("-------------------------------------")


print("Answer: ", ans)
# print array withoiut commas
print("Final Answer:", ",".join(map(str, ans)))

