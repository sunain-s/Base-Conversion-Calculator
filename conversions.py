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
    '''
    denary = int(denary)
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
    '''
    bcd = ''
    for den in str(denary):
        binary = den_to_n_base(int(den), 2)
        binary = leading_zeros(binary, 4)[::-1]
        bcd += f'{binary} '
    return bcd

def den_to_bin(denary, leading):
    '''
    Converts denary to binary via division method
    Secondary function only used in neg_den_to_twos_comp() function as is more convenient
    ==> leading = 8, gives a byte e.g. 11001 ==> 00011001
    '''
    denary = int(denary)
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
    '''
    Converts binary strings to denary via addition method
    '''
    binary = binary[::-1]
    denary = 0
    power = 0
    for bit in binary:
        if bit == '1':
            denary += 2**power
        power += 1
    return denary

def bin_to_hex(binary):
    '''
    Converts binary string into hexadecimal string
    uses denary conversions as intermediate steps
    '''
    denary = bin_to_den(binary)
    hexadecimal = den_to_n_base(denary, 16)
    return hexadecimal

def bin_to_octal(binary):
    '''
    Converts binary string into octal string
    uses denary conversions as intermediate steps
    '''
    denary = bin_to_den(binary)
    octal = den_to_n_base(denary, 8)
    return octal

def bin_to_bcd(binary):
    '''
    Converts binary string into binary coded decimal (BCD) string
    uses denary conversions as intermediate steps
    '''
    denary = bin_to_den(binary)
    bcd = den_to_bcd(denary)
    return bcd

# -------------------------------------------------------------------------------------------------
# Negative denary <==> negative binary conversions

def neg_den_to_twos_comp_bin(denary):
    '''
    Converts negative denary to Two's Complement binary string
    done via absolute binary value inversion and addition
    with denary conversions as intermediate steps
    '''
    denary *= -1
    abs_binary = leading_zeros(den_to_n_base(denary, 2), 8)[::-1]
    inverted_binary = binary_inversion(abs_binary)
    twos_comp_binary = den_to_bin(bin_to_den(inverted_binary) + 1, 8)[::-1]
    return twos_comp_binary
    
def twos_comp_bin_to_neg_den(binary):
    '''
    Converts Two's Complement binary string to negative denary
    done via subtraction and binary inversion
    with denary conversions as intermediate steps
    '''
    binary = den_to_n_base(bin_to_den(binary) - 1, 2)
    inverted_bin = binary_inversion(binary)
    denary = bin_to_den(inverted_bin)
    return f'-{denary}'

def neg_den_to_ones_comp_bin(denary):
    '''
    Converts negative denary to One's Complement binary string
    via binary inversion
    '''
    denary *= -1
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8)[::-1]
    ones_comp_bin = binary_inversion(binary)
    return ones_comp_bin

def den_to_sm_bin(denary):
    '''
    Converts positive or negative denary to its sign magnitude binary string
    by converting the value and adding a sign bit post conversion
    '''
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

def sm_bin_to_den(sm_binary):
    '''
    Converts sign magnitude binary string to negative denary
    by checking sign bit then using a string slice and conversion
    '''
    if sm_binary[0] == '0':
        denary = bin_to_den(sm_binary)
    elif sm_binary[0] == '1':
        sm_binary = sm_binary[1:]
        denary = f'-{bin_to_den(sm_binary)}'
    return denary

# -------------------------------------------------------------------------------------------------
# Hexadecimal ==> x conversions

def hex_to_den(hexadecimal):
    '''
    Converts hexadecimal string to denary using a hex indexing list and addition method
    '''
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    denary = 0
    power = 0
    hexadecimal = hexadecimal[::-1]
    for hex in hexadecimal:
        denary += hex_list.index(hex) * 16**power
        power += 1
    return denary

def hex_to_bin(hexadecimal):
    '''
    Converts hexadecimal string to binary string
    using denary conversions as intermediate steps
    '''
    hex = [hex for hex in hexadecimal]
    binary = ''
    for i in hex:
        denary = hex_to_den(i)
        nibble = den_to_n_base(denary, 2)
        binary += nibble
    return binary

def hex_to_octal(hexadecimal):
    '''
    Converts hexadecimal string to octal string
    using denary conversions as intermediate steps
    '''
    denary = hex_to_den(hexadecimal)
    octal = den_to_n_base(denary, 8)
    return octal

def hex_to_bcd(hexadecimal):
    '''
    Converts hexadecimal string to binary coded decimal string
    using denary conversions as intermediate steps
    '''
    denary = hex_to_den(hexadecimal)
    bcd = den_to_bcd(denary)
    return bcd

# -------------------------------------------------------------------------------------------------
# Octal ==> x conversions

def octal_to_den(octal):
    '''
    Converts octal string to denary via addition method
    '''
    octal = str(octal)[::-1]
    denary = 0
    power = 0
    for oct in octal:
        denary += int(oct) * 8 ** power
        power += 1
    return denary

def octal_to_bin(octal):
    '''
    Converts octal string to binary string
    via denary conversions as intermediate steps
    '''
    denary = octal_to_den(octal)
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8)[::-1]
    return binary
    
def octal_to_hex(octal):
    '''
    Converts octal string to hexadecimal string
    via denary conversions as intermediate steps
    '''
    denary = octal_to_den(octal)
    hexadecimal = den_to_n_base(denary, 16)
    return hexadecimal

def octal_to_bcd(octal):
    '''
    Converts octal string to binary coded decimal (BCD) string
    via denary conversions as intermediate steps
    '''
    denary = octal_to_den(octal)
    bcd = den_to_bcd(denary)
    return bcd

# -------------------------------------------------------------------------------------------------
# Binary Coded Decimal (BCD) ==> x conversions

def bcd_to_den(bcd):
    '''
    Converts binary coded decimal (BCD) string to denary
    using string addition - rather than numerical addition as used in other functions
    '''
    bcd = bcd.replace(' ', '')
    bcd = leading_zeros(bcd, 4)[::-1]
    nibble = ''
    denary =''
    for bit in bcd:
        nibble += bit
        if len(nibble) % 4 == 0:
            bcd = bcd[4:]
            denary += str(bin_to_den(nibble))
            nibble = ''
    return int(denary)

def bcd_to_bin(bcd):
    '''
    Converts binary coded decimal (BCD) to binary string
    using denary conversions as intermediate steps
    '''
    denary = bcd_to_den(bcd)
    binary = den_to_n_base(denary, 2)
    return binary

def bcd_to_hex(bcd):
    '''
    Converts binary coded decimal (BCD) to hexadecimal string
    using denary conversions as intermediate steps
    '''
    denary = bcd_to_den(bcd)
    hexadecimal = den_to_n_base(denary, 16)
    return hexadecimal

def bcd_to_octal(bcd):
    '''
    Converts binary coded decimal (BCD) to octal string
    using denary conversions as intermediate steps
    '''
    denary = bcd_to_den(bcd)
    octal = den_to_n_base(denary, 8)
    return octal

# -------------------------------------------------------------------------------------------------
# Denary, Binary, Hexadecimal Addition

def den_add_den(denary_one, denary_two):
    '''
    Adds 2 denary values together
    returns the result in denary form
    '''
    result = int(denary_one) + int(denary_two)
    return result

def den_add_bin(denary, binary):
    '''
    Adds a denary value to a binary value by converting both to denary
    returns the result in denary and binary forms
    '''
    bin_denary = bin_to_den(binary)
    result_den = denary + bin_denary
    result_bin = den_to_n_base(result_den, 2)
    return result_den, result_bin

def den_add_hex(denary, hexadecimal):
    '''
    Adds a denary value to a hexadecimal value by converting both to denary
    returns the result in denary and hexadecimal forms
    '''
    hex_denary = hex_to_den(hexadecimal)
    result_den = denary + hex_denary
    result_hex = den_to_n_base(result_den, 16)
    return result_den, result_hex

def bin_add_bin(binary_one, binary_two):
    '''
    Adds 2 binary values by converting both to denary
    returns the result in binary form
    '''
    denary_one = bin_to_den(binary_one)
    denary_two = bin_to_den(binary_two)
    result = denary_one + denary_two
    result = den_to_n_base(result, 2)
    return result

def bin_add_hex(binary, hexadecimal):
    '''
    Adds a binary value to a hexadecimal value by converting both to denary
    returns the result in binary and hexadecimal forms
    '''
    bin_denary = bin_to_den(binary)
    hex_denary = hex_to_den(hexadecimal)
    result_den = bin_denary + hex_denary
    result_bin = den_to_n_base(result_den, 2)        
    result_hex = den_to_n_base(result_den, 16)
    return result_bin, result_hex

def hex_add_hex(hex_one, hex_two):
    '''
    Adds 2 hexadecimal values by converting to denary
    returns the result in hexadecimal form
    '''
    denary_one = hex_to_den(hex_one)
    denary_two = hex_to_den(hex_two)
    result = denary_one + denary_two
    result = den_to_n_base(result, 16)
    return result

# -------------------------------------------------------------------------------------------------
# Denary, Binary, Hexadecimal Subtraction

def den_sub_den(denary_one, denary_two):
    '''
    Subtracts 1 denary value from another
    returns the result in denary form
    '''
    result = denary_one - denary_two
    return result

def den_sub_bin(denary, binary):
    '''
    Subtracts binary value from denary value by converting to denary
    returns the result in denary and binary forms
    '''
    bin_denary = bin_to_den(binary)
    result_den = denary - bin_denary
    if result_den < 0:
        result_bin = neg_den_to_twos_comp_bin(result_den)        
    else:
        result_bin = den_to_n_base(result_den, 2)
    return result_den, result_bin

def den_sub_hex(denary, hexadecimal):
    '''
    Subtracts hexadecimal value from denary value by converting to denary
    returns the result in denary and hexadecimal forms
    '''
    hex_denary = hex_to_den(hexadecimal)
    result_den = denary - hex_denary
    if result_den < 0:       
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}'
    else:
        result_hex = den_to_n_base(result_den, 16)
    return result_den, result_hex

def bin_sub_bin(binary_one, binary_two):
    '''
    Subtracts 2 binary value from another by converting to denary
    returns the result in binary form
    '''
    denary_one = bin_to_den(binary_one)
    denary_two = bin_to_den(binary_two)
    result_den = denary_one - denary_two
    if result_den < 0:
        result_bin = neg_den_to_twos_comp_bin(result_den)        
    else:
        result_bin = den_to_n_base(result_den, 2)
    return result_bin

def bin_sub_den(binary, denary):
    '''
    Subtracts denary value from binary value by converting to denary
    returns the result in binary and denary forms
    '''
    bin_denary = bin_to_den(binary)
    result_den = bin_denary - denary
    if result_den < 0:
        result_bin = neg_den_to_twos_comp_bin(result_den)        
    else:
        result_bin = den_to_n_base(result_den, 2)
    return result_bin, result_den

def bin_sub_hex(binary, hexadecimal):
    '''
    Subtracts hexadecimal value from binary value by converting to denary
    returns the result in binary and hexadecimal forms
    '''
    bin_denary = bin_to_den(binary)
    hex_denary = hex_to_den(hexadecimal)
    result_den = bin_denary - hex_denary
    if result_den < 0:
        result_bin = neg_den_to_twos_comp_bin(result_den)        
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}'
    else:
        result_bin = den_to_n_base(result_den, 2)
        result_hex = den_to_n_base(result_den, 16)
    return result_bin, result_hex

def hex_sub_hex(hex_one, hex_two):
    '''
    Subtracts 1 hexadecimal value from another by converting to denary
    returns the result in hexadecimal form
    '''
    denary_one = hex_to_den(hex_one)
    denary_two = hex_to_den(hex_two)
    result_den = denary_one - denary_two
    if result_den < 0:       
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}'
    else:
        result_hex = den_to_n_base(result_den, 16)
    return result_hex

def hex_sub_den(denary, hexadecimal):
    '''
    Subtracts denary value from hexadecimal value
    returns the result in hexadecimal and denary forms
    '''
    hex_denary = hex_to_den(hexadecimal)
    result_den = hex_denary - denary
    if result_den < 0:       
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}'
    else:
        result_hex = den_to_n_base(result_den, 16)
    return result_den, result_hex

def hex_sub_bin(hexadecimal, binary):
    '''
    Subtracts hexadecimal value from binary value by converting to denary
    returns the result in binary and hexadecimal forms
    '''
    bin_denary = bin_to_den(binary)
    hex_denary = hex_to_den(hexadecimal)
    result_den = hex_denary - bin_denary
    if result_den < 0:
        result_bin = neg_den_to_twos_comp_bin(result_den)        
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}'
    else:
        result_bin = den_to_n_base(result_den, 2)
        result_hex = den_to_n_base(result_den, 16)
    return result_hex, result_bin

# -------------------------------------------------------------------------------------------------