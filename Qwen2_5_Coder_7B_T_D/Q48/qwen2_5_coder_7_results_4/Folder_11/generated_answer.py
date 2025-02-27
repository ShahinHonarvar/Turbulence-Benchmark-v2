def return_binary_or_hexa(tup):
    a = tup[48]
    b = tup[76]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in tup[48:77]:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]