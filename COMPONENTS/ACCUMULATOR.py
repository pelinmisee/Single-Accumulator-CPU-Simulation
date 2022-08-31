from COMPONENTS.RAM import *
from COMPONENTS.PC import *
class ACCUMULATOR:
    def __init__(self):
        self.acc=0

    def BRZ(self, value, PC):
        current_pc = PC.getPC()
        PC.setPC(current_pc + int(value))
    def BRN(self,value, PC):
        current_pc = PC.getPC()
        PC.setPC(current_pc + int(value))
    def LDM(self, memAdress, opcode_HEX, RAM):
        self.acc= RAM.get_Val_of_register(memAdress,opcode_HEX)

    def LDI(self, value):
        self.acc=value

    def getAccVal(self):
        return self.acc

    def ADD(self, value):
        self.acc = self.acc + value

    def SUB(self,value):
        self.acc = self.acc - value

    def NEG(self):
        self.acc = -self.acc

    def MUL(self,value):
        self.acc = self.acc * value

    def DIV(self,value):
        self.acc = self.acc // value

    def LSL(self,value):
        self.acc = (2**value)*self.acc

    def LSR(self,value):
        self.acc = self.acc // (2**value)

    def XOR(self,value):
        self.acc = self.acc ^ value

    def NOT(self):
        self.acc = ~self.acc

    def AND(self,value):
        self.acc = self.acc & value

    def ORR(self,value):
        self.acc = self.acc | value
