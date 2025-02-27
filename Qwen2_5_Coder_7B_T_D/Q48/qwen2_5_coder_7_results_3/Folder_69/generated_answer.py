def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[a + 1:b]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]