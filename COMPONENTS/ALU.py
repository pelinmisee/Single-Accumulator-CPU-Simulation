from COMPONENTS.ACCUMULATOR import *
from COMPONENTS.RAM import *
from COMPONENTS.PC import *

class ALU:

    def operations(self, hex_op, memAdress, value, ACC , RAM, PC):
        if hex_op == '0x0':
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
            if(ACC.getAccVal() == 0):
                ACC.BRZ(value, PC)
            else:
                return
        elif hex_op == '0x1':
            self.showcurrent(hex_op, memAdress, value, ACC, RAM, PC)
            if (ACC.getAccVal() < 0):
                ACC.BRN(value, PC)
            else:
                return
        elif hex_op == '0x2':
            ACC.LDI(int(memAdress))
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x3':
            ACC.LDM(memAdress, hex_op,RAM)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x4':
            RAM.STR(memAdress, ACC.getAccVal())
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x5':
            ACC.ADD(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x6':
            ACC.SUB(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x7':
            ACC.MUL(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x8':
            ACC.DIV(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0x9':
            ACC.NEG()
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0xa':
            ACC.LSL(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0xb':
            ACC.LSR(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0xc':
            ACC.XOR(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0xd':
            ACC.NOT()
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0xe':
            ACC.AND(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        elif hex_op == '0xf':
            ACC.ORR(value)
            self.showcurrent(hex_op, memAdress, value, ACC , RAM, PC)
        else:
            print("Error")
            return
    def showcurrent(self,hex_op, memAdress, value, ACC , RAM, PC):
        print("PC = ", PC.getPC(), " ve  ACC = ", ACC.getAccVal(), "mem_str = ", hex_op)
