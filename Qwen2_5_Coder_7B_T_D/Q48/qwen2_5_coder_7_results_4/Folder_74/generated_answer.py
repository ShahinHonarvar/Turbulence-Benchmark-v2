def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    total_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a + 1 <= x <= b - 1, tup))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()