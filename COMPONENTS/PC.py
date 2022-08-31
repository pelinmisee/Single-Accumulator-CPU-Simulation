class PC:
    def __init__(self):
        self.pc = 0
    def getPC(self):
        return self.pc
    def setPC(self,value):
        self.pc = value
    def changePC(self,value, opcode_hex):
        if (opcode_hex == "0x0"):
            self.pc = int(value)
        else:
            return
