# Conversion Function file

# -------------------------------------------------------------------------------------------------
# Utility functions

def binary_inversion(binary):
    '''
    Inverts each bit in a binary string 
        1 ==> 0
        0 ==> 1
    Used for One's and Two's Complement 
    '''

    inverted_bin = ''
    for bit in binary:
        if bit == '0':
            bit = '1'
        elif bit == '1':
            bit = '0'
        inverted_bin += bit
    return inverted_bin

def leading_zeros(binary, length):
    '''
    Adds leading zeros to a binary string until a given length
        e.g. leading_zeros('11001', 8)
    returns '00011001' which is in byte form
    '''
    binary = binary[::-1]
    if len(binary) % length:
        zeros = length - (len(binary) % length)
        binary += '0' * zeros
    return binary

# -------------------------------------------------------------------------------------------------
# Denary ==> x conversions

def den_to_n_base(denary, base):
    '''
    Converts denary values to any base up to and including base-36
    denary - integer parameter, value being converted from
    base - integer parameter, base being converted to e.g. base = 2 outputs binary 
    '''
    base_num = ''
    if denary == 0:
        base_num = '0'
    while denary > 0:
        digit = int(denary % base)
        if digit < 10:
            base_num += str(digit)
        else:
            base_num += chr(ord('A') + digit - 10)
        denary //= base
    base_num = base_num[::-1]
    return base_num

def den_to_bcd(denary):
    '''
    Converts denary values to binary coded decimal
        e.g. 103 ==> 0001 0000 0011
    In BCD each nibble represents each digit - only 0000 to 1001 are used (0-9)
    denary - integer parameter, value being converted from
    '''
    bcd = ''
    for den in str(denary):
        binary = den_to_n_base(int(den), 2)
        binary = leading_zeros(binary, 4)[::-1]
        bcd += f'{binary} '
    return bcd

def den_to_bin(denary, leading):
    '''
    Converts denary to binary
    Secondary function only used in neg_den_to_twos_comp() function as is more convenient
    denary - integer parameter, value being converted from
    leading - integer parameter, for number of leading zeros to be calculated
        ==> leading - 8, gives a byte e.g. 11001 ==> 00011001
    '''
    binary = ''
    if denary < 0:
        denary *= -1
    while denary > 0:
        remainder = denary % 2
        binary += str(remainder)
        denary //= 2
    binary = leading_zeros(binary, leading)
    binary = binary[::-1]
    return binary

# -------------------------------------------------------------------------------------------------
# Binary ==> x conversions

def bin_to_den(binary):
    binary = binary[::-1]
    denary = 0
    power = 0
    for bit in binary:
        if bit == '1':
            denary += 2**power
        power += 1
    return denary

def bin_to_hex(binary):
    denary = bin_to_den(binary)
    hexadecimal = den_to_n_base(denary, 16)
    return hexadecimal

def bin_to_octal(binary):
    denary = bin_to_den(binary)
    octal = den_to_n_base(denary, 8)
    return octal

def bin_to_bcd(binary):
    denary = bin_to_den(binary)
    bcd = den_to_bcd(denary)
    return bcd

# -------------------------------------------------------------------------------------------------
# Negative denary <==> negative binary conversions

def neg_den_to_twos_comp_bin(denary):
    denary *= -1
    abs_binary = leading_zeros(den_to_n_base(denary, 2), 8)[::-1]
    inverted_binary = binary_inversion(abs_binary)
    twos_comp_binary = den_to_bin(bin_to_den(inverted_binary) + 1, 8)
    return twos_comp_binary
    
def twos_comp_bin_to_neg_den(binary): 
    binary = den_to_n_base(bin_to_den(binary) - 1, 2)
    inverted_bin = binary_inversion(binary)
    denary = bin_to_den(inverted_bin)
    return f'-{denary}'

def neg_den_to_ones_comp_bin(denary):
    denary *= -1
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8)[::-1]
    ones_comp_bin = binary_inversion(binary)
    return ones_comp_bin

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

# -------------------------------------------------------------------------------------------------
# Hexadecimal ==> x conversions

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

def hex_to_octal(hexadecimal):
    denary = hex_to_den(hexadecimal)
    octal = den_to_n_base(denary, 8)
    return octal

def hex_to_bcd(hexadecimal):
    denary = hex_to_den(hexadecimal)
    bcd = den_to_bcd(denary)
    return bcd

# -------------------------------------------------------------------------------------------------
# Octal ==> x conversions

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

def octal_to_bcd(octal):
    denary = octal_to_den(octal)
    bcd = den_to_bcd(denary)
    return bcd
# -------------------------------------------------------------------------------------------------
# Binary Coded Decimal (BCD) ==> x conversions
