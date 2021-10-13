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

def bin_to_den(binary):
    binary = binary[::-1]
    denary = 0
    power = 0
    for bit in binary:
        if bit == '1':
            denary += 2**power
        power += 1
    return denary

def den_to_bin(denary, leading):
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

def neg_den_to_twos_comp_bin(denary):
    binary = den_to_bin(denary, leading=8)
    inverted_bin = binary_inversion(binary)
    neg_binary = den_to_bin(bin_to_den(inverted_bin) + 1, leading=8)
    return neg_binary

def twos_comp_bin_to_neg_den(binary): 
    binary = den_to_bin(bin_to_den(binary) - 1, leading=8)
    inverted_bin = binary_inversion(binary)
    denary = bin_to_den(inverted_bin)
    return f'-{denary}'

def den_to_hex(denary):
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex = ''
    while denary > 0:
        remainder = denary % 16
        denary //= 16
        hex += hex_list[remainder]
    hex = hex[::-1]
    return hex
