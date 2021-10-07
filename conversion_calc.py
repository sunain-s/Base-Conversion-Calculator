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
