def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[3])
    total_sum = sum(range(a + 1, b)) - sum(set(tup[1:3]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()