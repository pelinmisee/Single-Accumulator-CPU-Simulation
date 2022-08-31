class RAM:
    def __init__(self):
        self.Reg_Dict = {}
        self.Reg_Order = 0
        self.Order_list = []

    def AddAdresses(self, reg_STR, opcode_HEX):
        #if opcode hex imiidiate geç
        if(opcode_HEX == "0x2"):
            return
        elif (opcode_HEX == "0x0"):
            return
        elif (opcode_HEX == "0x1"):
            return
        elif (opcode_HEX == "0x9"):
            return
        elif (opcode_HEX == "0xa"):
            return
        elif (opcode_HEX == "0xb"):
            return
        elif (opcode_HEX == "0xd"):
            return
        else:
            Add_Reg_STR = reg_STR
            self.Reg_Dict[Add_Reg_STR] = 0
    def showAdresses(self):
        return self.Reg_Dict

    def get_Val_of_register(self, reg_STR, opcode_HEX):
        if (opcode_HEX == "0x2"):
            return
        elif (opcode_HEX == "0x0"):
            return int(reg_STR)
        elif (opcode_HEX == "0x1"):
            return int(reg_STR)
        elif (opcode_HEX == "0x9"):
            return
        elif (opcode_HEX == "0xa"):
            return int(reg_STR)
        elif (opcode_HEX == "0xb"):
            return int(reg_STR)
        elif (opcode_HEX == "0xd"):
            return
        else:
            return self.Reg_Dict[reg_STR]

    def STR(self, reg_STR, value):
        self.Reg_Dict[reg_STR]=value

    def ADRESSORDER(self,reg_STR):
        self.Order_list.append(reg_STR)
