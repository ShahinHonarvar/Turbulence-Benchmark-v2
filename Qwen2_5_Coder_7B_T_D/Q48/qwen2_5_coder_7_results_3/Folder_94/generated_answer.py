def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in tup[a + 1:b]:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()