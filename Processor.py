import Conversion
import IAS

with open('machinecode.txt', 'r') as machineCode:
    machineLines = machineCode.readlines()

machineLines = [i.replace("\n", "") for i in machineLines]


class Processor:
    def __init__(self, Memory, PC, Instruction):
        self.Memory = Memory
        self.MAR = ""
        self.MBR = ""
        self.IBR = ""
        self.IR = ""
        self.AC = ""
        self.MQ = ""
        self.PC = PC
        self.Instruction = Instruction

    def FetchCycle(self):
        self.MAR = self.PC
        self.MBR = Instruction
        self.IBR = Instruction[self.PC][20:]
        self.IR = Instruction[self.PC][:8]
        self.MAR = Instruction[self.PC][8:20]
        if (self.IBR == " " * 20):
            self.PC += 1
        else:
            self.IR = self.IBR[:8]
            self.MAR = self.IBR[8:]
            self.PC += 1

    def ExecuteCycle(self):
        if self.IR == "00000001":
            self.MBR = self.MAR
            ias.LOAD(Conversion.BinaryToDecimal(self.MAR))
        elif self.IR == "00010011":
            ias.FACT()
        elif self.IR == "00010010":
            self.MBR = self.MAR
            ias.STOR(Conversion.BinaryToDecimal(self.MAR))
        elif self.IR == "00100100":
            self.MBR = self.MAR
            ias.PERM(Conversion.BinaryToDecimal(self.MAR))
        elif self.IR == "00001000":
            self.MBR = self.MAR
            ias.DIV(Conversion.BinaryToDecimal(self.MAR))
        elif self.IR == "00100101":
            self.MBR = self.MAR
            ias.LOADMQ()


# Creating and Assigning values to the variables into the Memory.

Memory = [""*40] * 1000

Memory[501] = Conversion.DecimalToBinaryNum(9)  # n
Memory[502] = Conversion.DecimalToBinaryNum(6)  # r

for i in range(0, len(machineLines)):
    Memory[i] = machineLines[i]

Instruction = machineLines.copy()


# Initializing the IAS System Components.

PC = 0
ias = IAS.IAS(Memory, PC)
processor = Processor(Memory, PC, Instruction)


# Running the IAS system, with some Test Cases.

print("Test Case 1:    n = 9, r = 6")
for i in range(len(Instruction)):
    processor.FetchCycle()
    processor.ExecuteCycle()

    print(f'PC = {processor.PC}')
    print(f'IR = {processor.IR},  MAR = {processor.MAR},  AC = {ias.AC},  IR = {
          processor.IR},  MAR = {processor.MAR},  AC = {ias.AC} \n')
print("Program Terminated.")
