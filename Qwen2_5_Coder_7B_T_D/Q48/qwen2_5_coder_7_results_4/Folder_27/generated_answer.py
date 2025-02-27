def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    total_sum = sum(range(a + 1, b)) - sum((i for i in range(a + 1, b) if i in tup[a + 1:b]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]