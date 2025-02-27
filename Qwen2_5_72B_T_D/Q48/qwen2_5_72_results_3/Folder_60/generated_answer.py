def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    present = set(tup[39:52])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]