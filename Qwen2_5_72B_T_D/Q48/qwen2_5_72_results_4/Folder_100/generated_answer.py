def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[78]
    present = set(tup[45:78])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]