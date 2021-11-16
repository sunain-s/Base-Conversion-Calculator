# Conversion Function file

# -------------------------------------------------------------------------------------------------
# Frequent Comments

'''
string = string[::-1] 
  ==> reverses string

denary *= -1
  ==> making absolute denary value
'''

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
        binary += '0' * zeros # packs necessary amount of leading zeros into string
    return binary # returns reversed binary (must be reversed later in process)

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
    while denary > 0: # loops until no remainder
        digit = int(denary % base) # division method of conversion
        if digit < 10:
            base_num += str(digit) # adds 0-9 
        else:
            base_num += chr(ord('A') + digit - 10) # adds A-Z
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
        binary = den_to_n_base(int(den), 2) # converts each digit to binary
        binary = leading_zeros(binary, 4)[::-1] # makes each digit a nibble
        bcd += f'{binary} ' # creates bcd string with spaces between nibbles
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
    while denary > 0: # loops until no remainder
        remainder = denary % 2 # division method of converting
        binary += str(remainder) # adds to binary string
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
            denary += 2**power # addition method of converting
        power += 1 # uses place values
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

    denary = int(denary)
    denary *= -1 
    abs_binary = leading_zeros(den_to_n_base(denary, 2), 16)[::-1] #converts to binary with 2 bytes
    inverted_binary = binary_inversion(abs_binary)
    twos_comp_binary = den_to_bin(bin_to_den(inverted_binary) + 1, 8)[::-1] # adds 1 to inverted then converts back to binary
    return twos_comp_binary
    
def twos_comp_bin_to_neg_den(binary):
    '''
    Converts Two's Complement binary string to negative denary
    done via subtraction and binary inversion
    with denary conversions as intermediate steps
    '''

    binary = den_to_n_base(bin_to_den(binary) - 1, 2) # subtracts 1 in denary then converts back to binary
    inverted_bin = binary_inversion(binary)
    denary = bin_to_den(inverted_bin) # converts to absolute denary value
    return f'-{denary}' 

def neg_den_to_ones_comp_bin(denary):
    '''
    Converts negative denary to One's Complement binary string
    via binary inversion
    '''

    denary = int(denary)
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

    denary = int(denary)
    if denary < 0:
        abs_den = denary * -1
    else:
        abs_den = denary
    binary = den_to_n_base(abs_den, 2)
    binary = binary[::-1]
    if denary < 0: # adds sign bit based on direction
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

    # checks sign bit
    if sm_binary[0] == '0':
        denary = bin_to_den(sm_binary)
    elif sm_binary[0] == '1':
        sm_binary = sm_binary[1:] # removes sign bit if negative
        denary = f'-{bin_to_den(sm_binary)}' # converts then adds '-'
    return denary

def twos_comp_to_sm_bin(twos_comp):
    '''
    Converts Two's Complement binary to sign magnitude binary
    by converting to denary
    '''

    denary = twos_comp_bin_to_neg_den(twos_comp)
    sm_bin = den_to_sm_bin(int(denary))
    return sm_bin

def twos_comp_to_ones_comp(twos_comp):
    '''
    Converts Two's Complement binary to One's Complement binary
    by converting to denary
    '''
    
    denary = twos_comp_bin_to_neg_den(twos_comp)
    ones_comp = neg_den_to_ones_comp_bin(int(denary))
    return ones_comp

def bin_to_sm_bin(binary):
    '''
    Converts unsigned binary to sign magnitude binary
    by converting to denary
    '''

    denary = bin_to_den(binary)
    sm_bin = den_to_sm_bin(denary)
    return sm_bin

# -------------------------------------------------------------------------------------------------
# Hexadecimal ==> x conversions

def hex_to_den(hexadecimal):
    '''
    Converts hexadecimal string to denary using a hex indexing list and addition method
    '''

    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'] # possible hex digits
    denary = 0
    power = 0
    hexadecimal = hexadecimal[::-1]
    for hex in hexadecimal:
        denary += hex_list.index(hex) * 16**power # addition method of comverting
        power += 1 # uses places values
    return denary

def hex_to_bin(hexadecimal):
    '''
    Converts hexadecimal string to binary string
    using denary conversions as intermediate steps
    '''

    binary = ''
    denary = hex_to_den(hexadecimal)
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8)[::-1]
    # converts to positive sign magnitude binary
    if binary[0] == '1':
        binary = binary[::-1]
        binary += '0'
    return binary[::-1]

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
        denary += int(oct) * 8 ** power # addition method od converting
        power += 1 # uses place values
    return denary

def octal_to_bin(octal):
    '''
    Converts octal string to binary string
    via denary conversions as intermediate steps
    '''

    denary = octal_to_den(octal)
    binary = den_to_n_base(denary, 2)
    binary = leading_zeros(binary, 8) # makes binary into byte form
    binary += '0' # adds sign bit
    return binary[::-1]
    
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

    bcd = bcd.replace(' ', '') # removes all spaces in input
    bcd = leading_zeros(bcd, 4)[::-1] # adds any leading zeros that are necessary
    nibble = ''
    denary =''
    # adds each bit to nibble then adds nibble to denary
    for bit in bcd:
        nibble += bit
        if len(nibble) % 4 == 0:
            bcd = bcd[4:] # slices bcd string to remove 4 bits that have been looped through
            denary += str(bin_to_den(nibble))
            nibble = '' # resets nibble 
    return int(denary)

def bcd_to_bin(bcd):
    '''
    Converts binary coded decimal (BCD) to binary string
    using denary conversions as intermediate steps
    '''

    denary = bcd_to_den(bcd)
    binary = den_to_n_base(denary, 2)[::-1]
    binary += '0' # adds sign bit for sign magnitude
    return binary[::-1]

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
    result_den = int(denary) + bin_denary
    result_bin = den_to_n_base(result_den, 2)
    return result_den, result_bin

def den_add_hex(denary, hexadecimal):
    '''
    Adds a denary value to a hexadecimal value by converting both to denary
    returns the result in denary and hexadecimal forms
    '''

    hex_denary = hex_to_den(hexadecimal)
    result_den = int(denary) + hex_denary
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

    result = int(denary_one) - int(denary_two)
    return result

def den_sub_bin(denary, binary):
    '''
    Subtracts binary value from denary value by converting to denary
    returns the result in denary and binary forms
    '''

    bin_denary = bin_to_den(binary)
    result_den = int(denary) - bin_denary
    # accounts for negative binary and represents in negative two's complement
    if result_den < 0:
        result_bin = f"Two's complement; {neg_den_to_twos_comp_bin(result_den)}"
    else:
        result_bin = den_to_n_base(result_den, 2)
    return result_den, result_bin

def den_sub_hex(denary, hexadecimal):
    '''
    Subtracts hexadecimal value from denary value by converting to denary
    returns the result in denary and hexadecimal forms
    '''

    hex_denary = hex_to_den(hexadecimal)
    result_den = int(denary) - hex_denary
    # accounts for negative hexadecimal
    if result_den < 0:   
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}' # adds '-' sign in front of absolute value
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
    # accounts for negative binary
    if result_den < 0:
        result_bin = f"Two's complement; {neg_den_to_twos_comp_bin(result_den)}" # represents binary in two's complement
    else:
        result_bin = den_to_n_base(result_den, 2)
    return result_bin

def bin_sub_den(binary, denary):
    '''
    Subtracts denary value from binary value by converting to denary
    returns the result in binary and denary forms
    '''

    bin_denary = bin_to_den(binary)
    result_den = bin_denary - int(denary)
    # accounts for negative binary
    if result_den < 0:
        result_bin = f"Two's complement; {neg_den_to_twos_comp_bin(result_den)}" # represents binary in two's complement   
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
    # accounts for negative binary and negative hexadecimal
    if result_den < 0:
        result_bin = f"Two's complement; {neg_den_to_twos_comp_bin(result_den)}" # represents binary in two's complement 
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}' # adds '-' in front of absolute hexadecimal 
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
    # accounts for negative hexadecimal
    if result_den < 0:       
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}' # adds '-' in front of absolute hexadecimal
    else:
        result_hex = den_to_n_base(result_den, 16)
    return result_hex

def hex_sub_den(hexadecimal, denary):
    '''
    Subtracts denary value from hexadecimal value
    returns the result in hexadecimal and denary forms
    '''

    hex_denary = hex_to_den(hexadecimal)
    result_den = hex_denary - int(denary)
    # accounts for negative hexadecimal
    if result_den < 0:       
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}' # adds '-' in front of absolute hexadecimal
    else:
        result_hex = den_to_n_base(result_den, 16)
    return result_hex, result_den

def hex_sub_bin(hexadecimal, binary):
    '''
    Subtracts hexadecimal value from binary value by converting to denary
    returns the result in binary and hexadecimal forms
    '''

    bin_denary = bin_to_den(binary)
    hex_denary = hex_to_den(hexadecimal)
    result_den = hex_denary - bin_denary
    # accounts for negative hexadecimal and negative binary
    if result_den < 0:
        result_bin = f"Two's complement; {neg_den_to_twos_comp_bin(result_den)}" # represents binary in two's complement
        result_hex = f'-{den_to_n_base(result_den * -1, 16)}' # adds '-' in front of absolute hexadecimal value
    else:
        result_bin = den_to_n_base(result_den, 2)
        result_hex = den_to_n_base(result_den, 16)
    return result_hex, result_bin

# -------------------------------------------------------------------------------------------------
# Test Site
