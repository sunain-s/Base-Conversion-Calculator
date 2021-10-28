def binary_inversion(binary):
    inverted_bin = ''
    for bit in binary:
        if bit == '0':
            bit = '1'
        elif bit == '1':
            bit = '0'
        inverted_bin += bit
    return inverted_bin

def leading_zeros(binary, length):
    binary = binary[::-1]
    if len(binary) % length:
        zeros = length - (len(binary) % length)
        binary += '0' * zeros
    return binary

def den_to_n_base(denary, base):
    base_num = ''
    while denary > 0:
        digit = int(denary % base)
        if digit < 10:
            base_num += str(digit)
        else:
            base_num += chr(ord('A') + digit - 10)
        denary //= base
    base_num = base_num[::-1]
    return base_num

def bin_to_den(binary):
    binary = binary[::-1]
    denary = 0
    power = 0
    for bit in binary:
        if bit == '1':
            denary += 2**power
        power += 1
    return denary

def neg_den_to_twos_comp_bin(denary):
    length = len(den_to_n_base(denary * -1, 2)) + 1
    s = bin(denary & int('1' * length, 2))[2:]
    return ("{0:0>%s}" % length).format(s)

def twos_comp_bin_to_neg_den(binary): 
    binary = den_to_n_base(bin_to_den(binary) - 1, 2)
    inverted_bin = binary_inversion(binary)
    denary = bin_to_den(inverted_bin)
    return f'-{denary}'

def bin_to_hex(binary):
    denary = bin_to_den(binary)
    hexadecimal = den_to_n_base(denary, 16)
    return hexadecimal

def hex_to_den(hexadecimal):
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    denary = 0
    power = 0
    hexadecimal = hexadecimal[::-1]
    for hex in hexadecimal:
        denary += hex_list.index(hex) * 16**power
        power += 1
    return denary

def hex_to_bin(hexadecimal):
    hex = [hex for hex in hexadecimal]
    binary = ''
    for i in hex:
        denary = hex_to_den(i)
        nibble = den_to_n_base(denary, 2)
        binary += nibble
    return binary

def den_to_sm_bin(denary):
    if denary < 0:
        abs_den = denary * -1
    else:
        abs_den = denary
    binary = den_to_n_base(abs_den, 2)
    binary = binary[::-1]
    if denary < 0:
        binary += '1'
    else:
        binary += '0'
    binary = binary[::-1]
    return binary
    
def neg_den_to_ones_comp_bin(denary):
    denary *= -1
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8)[::-1]
    ones_comp_bin = binary_inversion(binary)
    return ones_comp_bin

def octal_to_den(octal):
    octal = str(octal)[::-1]
    denary = 0
    power = 0
    for oct in octal:
        denary += int(oct) * 8 ** power
        power += 1
    return denary

def octal_to_bin(octal):
    denary = octal_to_den(octal)
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8)[::-1]
    return binary
    
def octal_to_hex(octal):
    denary = octal_to_den(octal)
    hexadecimal = den_to_n_base(denary, 16)
    return hexadecimal
