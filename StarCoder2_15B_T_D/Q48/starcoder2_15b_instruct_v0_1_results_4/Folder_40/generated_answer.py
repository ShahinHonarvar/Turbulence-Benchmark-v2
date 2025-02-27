def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[3])
    odd_sum = 0
    for i in range(a + 1, b):
        if i not in tup:
            odd_sum += i
    if odd_sum % 2 == 1:
        return bin(odd_sum)[2:]
    elif odd_sum == 0:
        return ''
    else:
        return hex(odd_sum)[2:].upper()