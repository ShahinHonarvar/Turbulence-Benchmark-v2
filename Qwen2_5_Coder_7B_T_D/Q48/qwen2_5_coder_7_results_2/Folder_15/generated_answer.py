def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[4])
    total_sum = sum(range(a + 1, b)) - sum((tup[i] for i in range(1, 4)))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()