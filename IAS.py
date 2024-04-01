from math import factorial
from Conversion import BinaryToDecimal, DecimalToBinaryNum


class IAS:
    def __init__(self, Memory, PC):
        self.Memory = Memory
        self.MAR = ""
        self.MBR = ""
        self.IBR = ""
        self.IR = ""
        self.AC = ""
        self.MQ = ""
        self.PC = PC

    def LOAD(self, address):
        self.AC = self.Memory[address]

    def LOADMQ(self):
        self.AC = self.MQ

    def LOADabs(self, address):
        self.AC = "0" + self.Memory[address][1:]

    def LOADnegative(self, address):
        if self.Memory[address][0] == '1':
            self.AC = "0" + self.Memory[address][1:]
        else:
            self.AC = "1" + self.Memory[address][1:]

    def SUB(self, address):
        signac = 1
        sign_mem = 1
        if self.AC[0] == '1':
            signac = -1
        if self.Memory[address][0] == '1':
            sign_mem = -1
        ac = BinaryToDecimal(self.AC[1:])
        mem = BinaryToDecimal(self.Memory[address][1:])
        ac = signac * ac - sign_mem * mem
        if ac > 0:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]
        else:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]

    def SUBabs(self, address):
        signac = 1
        if self.AC[0] == '1':
            signac = -1
        ac = BinaryToDecimal(self.AC[1:])
        mem = BinaryToDecimal(self.Memory[address][1:])
        ac = signac * ac - mem
        if ac > 0:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]
        else:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]

    def DIV(self, address):
        signac = 1
        sign_mem = 1
        if self.AC[0] == '1':
            signac = -1
        if self.Memory[address][0] == '1':
            sign_mem = -1
        ac = BinaryToDecimal(self.AC[1:])
        mem = BinaryToDecimal(self.Memory[address][1:])

        if (mem == 0):
            mem = 1
        mq = (signac * ac) // (sign_mem * mem)
        ac = (signac * ac) % (sign_mem * mem)

        if ac > 0:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]
        else:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]
        if mq > 0:
            self.MQ = "0" + DecimalToBinaryNum(mq)[1:]
        else:
            self.MQ = "1" + DecimalToBinaryNum(abs(mq))[1:]

    def JUMPright(self, address):
        self.PC = address

    def JUMPleft(self, address):
        self.PC = address

    def JUMPcondRight(self, address):
        if self.AC[0] == '0':
            self.PC = address
            return True
        return False

    def JUMPcondLeft(self, address):
        if self.AC[0] == '0':
            self.PC = address
            return True
        return False

    def ADD(self, address):
        signac = 1
        sign_mem = 1
        if self.AC[0] == '1':
            signac = -1
        if self.Memory[address][0] == '1':
            sign_mem = -1
        ac = BinaryToDecimal(self.AC[1:])
        mem = BinaryToDecimal(self.Memory[address][1:])
        ac = signac * ac + sign_mem * mem
        if ac < 0:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]
        else:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]

    def ADDabs(self, address):
        signac = 1
        if self.AC[0] == '1':
            signac = -1
        ac = BinaryToDecimal(self.AC[1:])
        mem = BinaryToDecimal(self.Memory[address][1:])
        ac = signac * ac + mem
        if ac > 0:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]
        else:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]

    def LSH(self):
        signac = 1
        if self.AC[0] == '1':
            signac = -1
        ac = BinaryToDecimal(self.AC[1:])
        ac = signac * ac * 2
        if ac > 0:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]
        else:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]

    def RSH(self):
        signac = 1
        if self.AC[0] == '1':
            signac = -1
        ac = BinaryToDecimal(self.AC[1:])
        ac = signac * (ac // 2)
        if ac > 0:
            self.AC = "0" + DecimalToBinaryNum(ac)[1:]
        else:
            self.AC = "1" + DecimalToBinaryNum(abs(ac))[1:]

    def STOR(self, address):
        self.Memory[address] = self.AC
        print(f"STORED into Memory({address}) = {self.Memory[address]}\n")

    def FACT(self):
        signac = 1
        if self.AC[0] == '1':
            signac = -1
        ac = BinaryToDecimal(self.AC[1:])
        ac = signac * factorial(ac)
        self.AC = "0" + DecimalToBinaryNum(ac)[1:]

    def PERM(self, address):
        signac = 1
        sign_mem = 1
        if self.AC[0] == '1':
            signac = -1
        if self.Memory[address][0] == '1':
            sign_mem = -1
        ac = signac * BinaryToDecimal(self.AC[1:])
        mem = sign_mem * BinaryToDecimal(self.Memory[address][1:])

        fact_ac = factorial(ac)
        if (ac - mem > 0):
            tmp = ac - mem
        else:
            print("Error r cannout be greator than n")

        fact_mem = factorial(tmp)

        res = fact_ac // fact_mem

        self.AC = "0" + DecimalToBinaryNum(res)[1:]
