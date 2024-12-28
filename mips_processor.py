def decimal_to_binary(decimal):
    # Convert negative decimal numbers to 2's complement form
    if decimal < 0:
        binary_str = bin(abs(decimal))[2:].zfill(32)
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        binary_str = bin(int(inverted_bits, 2) + 1)[2:].zfill(32)
    else:
        binary_str = bin(decimal)[2:].zfill(32)
    return binary_str

def binary_to_decimal(binary_str):
    # Check if the binary string represents a negative number
    if binary_str[0] == '1':
        binary_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
        decimal = int(binary_str, 2) + 1
        return -decimal
    else:
        return int(binary_str, 2)

reg_zero = '0'*32
reg_at = '0'*32
reg_v0 = '0'*32
reg_v1 = '0'*32
reg_a0 = '0'*32
reg_a1 = '0'*32
reg_a2 = '0'*32
reg_a3 = '0'*32
reg_t0 = '0'*32
reg_t1 = '0'*32
reg_t2 = '0'*32
reg_t3 = '0'*32
reg_t4 = '0'*32
reg_t5 = '0'*32
reg_t6 = '0'*32
reg_t7 = '0'*32
reg_s0 = '0'*32
reg_s1 = '0'*32
reg_s2 = '0'*32
reg_s3 = '0'*32
reg_s4 = '0'*32
reg_s5 = '0'*32
reg_s6 = '0'*32
reg_s7 = '0'*32
reg_t8 = '0'*32
reg_t9 = '0'*32
reg_k0 = '0'*32
reg_k1 = '0'*32
reg_gp = '0'*32
reg_sp = '0'*32
reg_fp = '0'*32
reg_ra = '0'*32
pc = '00000000010000000000000000000000'
hi = '0'*32
lo = '0'*32

registers = [reg_zero, reg_at, reg_v0, reg_v1, reg_a0, reg_a1, reg_a2, reg_a3, reg_t0, reg_t1, reg_t2, reg_t3, reg_t4, reg_t5, reg_t6, reg_t7, reg_s0, reg_s1, reg_s2, reg_s3, reg_s4, reg_s5, reg_s6, reg_s7, reg_t8, reg_t9, reg_k0, reg_k1, reg_gp, reg_sp, reg_fp, reg_ra]


memory = {}
address = 4194304
with open('./dumped/armstrong_text_machine','r') as file:
    for line in file:
        memory[address] = line[0:8]
        memory[address+1] = line[8:16]
        memory[address+2] = line[16:24]
        memory[address+3] = line[24:32]
        address += 4

address = 268500992

with open('./dumped/armstrong_data_machine','r') as file:
    for line in file:
        memory[address] = line[0:8]
        memory[address+1] = line[8:16]
        memory[address+2] = line[16:24]
        memory[address+3] = line[24:32]
        address += 4

while (True):
    print(int(pc,2))
    print("Instruction Fetch Begins")
    print("-"*10)
    instruction = memory[int(pc,2)] + memory[int(pc,2) + 1] + memory[int(pc,2) + 2] + memory[int(pc,2) + 3]
    print("Instruction Fetch Ends")
    print("-"*10)
    print("Instruction Decode Begins")
    print("-"*10)
    
    if (instruction[0:6] == '001111'): #lui
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        immediate = immediate + '0'*16
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        registers[int(rt,2)] = immediate
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)

    
    elif (instruction[0:6] == '100011'): #lw
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = binary_to_decimal(registers[int(rs,2)]) + binary_to_decimal(immediate)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        temp = memory[alu] + memory[alu+1] + memory[alu+2] + memory[alu+3]
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        registers[int(rt,2)] = temp
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)

    elif (instruction[0:6] == '001001'): #addiu 
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = int(registers[int(rs,2)],2) + int(immediate,2)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        registers[int(rt,2)] = bin(alu)[2:].zfill(32)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)

    elif (instruction[0:6] == '000101'): #bne
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = int(registers[int(rs,2)],2) - int(registers[int(rt,2)],2)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)
        if (alu != 0):
            pc = bin(int(pc,2) + binary_to_decimal(immediate)*4)[2:].zfill(32)

    elif (instruction[0:6] == '000100'): #beq
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = int(registers[int(rs,2)],2) - int(registers[int(rt,2)],2)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)
        if (alu == 0):
            pc = bin(int(pc,2) + binary_to_decimal(immediate)*4)[2:].zfill(32)

    elif (instruction[0:6] == '001000'): #addi
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = binary_to_decimal(registers[int(rs,2)]) + binary_to_decimal(immediate)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        registers[int(rt,2)] = decimal_to_binary(alu)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)
    
    elif (instruction[0:6] == '001101'): #ori
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = binary_to_decimal(registers[int(rs,2)]) | binary_to_decimal(immediate)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        registers[int(rt,2)] = decimal_to_binary(alu)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)

    elif (instruction[0:6] == '101011'): #sw
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        immediate = instruction[16:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        alu = binary_to_decimal(registers[int(rs,2)]) + binary_to_decimal(immediate)
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        memory[alu] = registers[int(rt,2)][0:8]
        memory[alu+1] = registers[int(rt,2)][8:16]
        memory[alu+2] = registers[int(rt,2)][16:24]
        memory[alu+3] = registers[int(rt,2)][24:32]
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)

    elif (instruction[0:6] == '000010'): #j
        op = instruction[0:6]
        address = instruction[6:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        address = '0'*4 + address + '0'*2
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)
        pc = address

    elif (instruction[0:6] == '011100'): #mul
        op = instruction[0:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        rd = instruction[16:21]
        shift = instruction[21:26]
        function = instruction[26:32]
        print("Instruction Decode Ends")
        print("-"*10)
        print("Execute Begins")
        print("-"*10)
        result = binary_to_decimal(registers[int(rs,2)]) * binary_to_decimal(registers[int(rt,2)])
        print("Execute Ends")
        print("-"*10)
        print("Memory Access Begins")
        print("-"*10)
        print("Memory Access Ends")
        print("-"*10)
        print("Write Back Begins")
        print("-"*10)
        registers[int(rd,2)] = decimal_to_binary(result)
        print("Write Back Ends")
        print("-"*10)
        pc = bin(int(pc,2) + 4)[2:].zfill(32)


    elif (instruction[0:6] == '000000'): #r-format instruction
        if (instruction[26:32] == '100000'): #add
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            result = binary_to_decimal(registers[int(rs,2)]) + binary_to_decimal(registers[int(rt,2)])
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            registers[int(rd,2)] = decimal_to_binary(result)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '100010'): #sub
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            result = binary_to_decimal(registers[int(rs,2)]) - binary_to_decimal(registers[int(rt,2)])
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            registers[int(rd,2)] = decimal_to_binary(result)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '011010'): #div
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            q = binary_to_decimal(registers[int(rs,2)]) // binary_to_decimal(registers[int(rt,2)])
            r = binary_to_decimal(registers[int(rs,2)]) % binary_to_decimal(registers[int(rt,2)])
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            hi = decimal_to_binary(r)
            lo = decimal_to_binary(q)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '010010'): #mflo
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            alu = binary_to_decimal(lo)
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            registers[int(rd,2)] = decimal_to_binary(alu)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '010000'): #mfhi
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            alu = binary_to_decimal(hi)
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            registers[int(rd,2)] = decimal_to_binary(alu)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '101010'): #slt
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            if (binary_to_decimal(registers[int(rs,2)]) < binary_to_decimal(registers[int(rs,2)])):
                result = 1
            else:
                result = 0
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            registers[int(rd,2)] = decimal_to_binary(result)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '100011'): #subu
            op = instruction[0:6]
            rs = instruction[6:11]
            rt = instruction[11:16]
            rd = instruction[16:21]
            shift = instruction[21:26]
            function = instruction[26:32]
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            result = int(registers[int(rs,2)],2) - int(registers[int(rt,2)],2)
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            registers[int(rd,2)] = decimal_to_binary(result)
            print("Write Back Ends")
            print("-"*10)
            pc = bin(int(pc,2) + 4)[2:].zfill(32)

        elif (instruction[26:32] == '001100'): #syscall
            print("Instruction Decode Ends")
            print("-"*10)
            print("Execute Begins")
            print("-"*10)
            print("Execute Ends")
            print("-"*10)
            print("Memory Access Begins")
            print("-"*10)
            print("Memory Access Ends")
            print("-"*10)
            print("Write Back Begins")
            print("-"*10)
            print("Write Back Ends")
            print("-"*10)
            if (int(registers[2],2) == 1):
                print(binary_to_decimal(registers[4]))
                print('-'*10)
                pc = bin(int(pc,2) + 4)[2:].zfill(32)
            elif (int(registers[2],2) == 10):
                print(memory[268501027])
                break