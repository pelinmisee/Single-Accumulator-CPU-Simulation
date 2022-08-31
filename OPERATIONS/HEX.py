class HEX:
    def __init__(self):
        self.Hex_List = []


    def obtain_opcode_hex(self,opcode_bin):

        dec=int(opcode_bin[0])*8+ int(opcode_bin[1])*4+int(opcode_bin[2])*2+int(opcode_bin[3])
        opcode_hex=hex(dec)

        return opcode_hex
    def AddOperations(self, op_hex):
        self.Hex_List.append(op_hex)

    def showOperations(self):
        return self.Hex_List

    def getHexlist(self):
        return self.Hex_List
