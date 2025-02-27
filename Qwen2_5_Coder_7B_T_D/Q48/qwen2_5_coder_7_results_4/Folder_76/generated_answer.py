def return_binary_or_hexa(tup):
    a = tup[450]
    b = tup[905]
    total_sum = sum((i for i in range(a + 1, b) if i not in tup[a:b + 1]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()