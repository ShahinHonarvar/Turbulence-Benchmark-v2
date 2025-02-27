def return_binary_or_hexa(tup):
    a = tup[48]
    b = tup[76]
    present = set(tup[49:76])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum == 0:
        return ''
    else:
        return hex(missing_sum)[2:]