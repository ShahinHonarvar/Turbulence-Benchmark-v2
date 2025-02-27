def return_binary_or_hexa(tup):
    a = tup[32]
    b = tup[44]
    total_sum = sum(range(a + 1, b)) - sum((x for x in tup if a < x < b))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]