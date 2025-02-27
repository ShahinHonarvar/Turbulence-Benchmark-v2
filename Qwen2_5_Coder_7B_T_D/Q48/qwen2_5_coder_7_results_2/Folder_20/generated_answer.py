def return_binary_or_hexa(tup):
    a = tup[27]
    b = tup[96]
    total_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(tup.index(a), tup.index(b) + 1)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()