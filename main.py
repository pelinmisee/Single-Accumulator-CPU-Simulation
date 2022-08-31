from OPERATIONS.Text import *
from OPERATIONS.HEX import *
from OPERATIONS.OPCODE import *
from COMPONENTS.ACCUMULATOR import *
from COMPONENTS.ALU import *
from COMPONENTS.RAM import *
from COMPONENTS.PC import *
RAM = RAM()
ALU = ALU()
HEX = HEX()
OPCODE = OPCODE()
PC = PC()
text=Text("deneme.txt")
ACC = ACCUMULATOR() #ACCUMULATORU 0'DAN BASLATIYOZ HER ÇALIŞTIRILDIĞINDA 0'A EŞİT OLACAK
print("before operations acc = " , ACC.getAccVal())
for i in range(1,text.total_of_row()+1):  #bu for her satır işlemi için tamamlanacak olan for.
    line=text.getting_line(i)
    opcode_STR, reg_STR=OPCODE.obtain_opcode_str(line)
    opcode_BIN=OPCODE.obtain_opcode_bin(opcode_STR)
    opcode_HEX=HEX.obtain_opcode_hex(opcode_BIN)
    RAM.AddAdresses(reg_STR,opcode_HEX)
    RAM.ADRESSORDER(reg_STR)
    HEX.AddOperations(opcode_HEX)

print(HEX.Hex_List, RAM.showAdresses())


while PC.getPC() < len(HEX.getHexlist()):  #bu for her satır işlemi için tamamlanacak olan for.
    opcode_HEX = HEX.getHexlist()[PC.getPC()]
    mem_STR = RAM.Order_list[PC.getPC()]
    ALU.operations(opcode_HEX,mem_STR,RAM.get_Val_of_register(mem_STR, opcode_HEX),ACC, RAM, PC)
    if(opcode_HEX == "0x0"):
        pass
    elif(opcode_HEX == "0x1"):
        pass
    else:
        PC.setPC(PC.getPC() + 1)
    print(RAM.showAdresses())
    input()









