def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[100]
    missing = [i for i in range(a + 1, b) if i not in tup[a + 1:b]]
    total_sum = sum(missing)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()