def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in tup[44:92]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()