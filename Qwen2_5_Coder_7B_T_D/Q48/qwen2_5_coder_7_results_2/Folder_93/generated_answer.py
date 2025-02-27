def return_binary_or_hexa(tup):
    a, b = (tup[57], tup[85])
    total_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(58, 85)))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]