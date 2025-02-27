def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    total_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(a + 1, b) if tup[i] in tup))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()