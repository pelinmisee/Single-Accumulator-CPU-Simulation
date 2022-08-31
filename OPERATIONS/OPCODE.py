class OPCODE:
    def obtain_opcode_str(self, line):
        opcode_str=line.split(" ")
        opcode_bin_str=opcode_str[0].upper()
        opcode_reg_str = opcode_str[1].upper().replace("\n", "")
        if(len(opcode_reg_str) == 2):
            return opcode_bin_str,opcode_reg_str
        else:
            opcode_reg_str_new = "0"+opcode_reg_str
            return opcode_bin_str,opcode_reg_str_new

    def obtain_opcode_bin(self,opcode_str):
        opcode_bin=""
        if opcode_str == "BRZ":
            opcode_bin="0000"
        elif opcode_str == "BRN":
            opcode_bin="0001"
        elif opcode_str == "LDI":
            opcode_bin="0010"
        elif opcode_str == "LDM":
            opcode_bin="0011"
        elif opcode_str == "STR":
            opcode_bin="0100"
        elif opcode_str == "ADD":
            opcode_bin="0101"
        elif opcode_str == "SUB":
            opcode_bin="0110"
        elif opcode_str == "MUL":
            opcode_bin="0111"
        elif opcode_str == "DIV":
            opcode_bin="1000"
        elif opcode_str == "NEG":
            opcode_bin="1001"
        elif opcode_str == "LSL":
            opcode_bin="1010"
        elif opcode_str == "LSR":
            opcode_bin="1011"
        elif opcode_str == "XOR":
            opcode_bin="1100"
        elif opcode_str == "NOT":
            opcode_bin="1101"
        elif opcode_str == "AND":
            opcode_bin="1110"
        elif opcode_str == "ORR":
            opcode_bin="1111"
        # else:
        #     print ("Opcode is not available") bunu işin içine katınca hexte sorun çıkıyo AMA OPCODEUN YANLIŞ OLMASI DURUMU İÇİN BİŞEY YAPILMALI
        return opcode_bin