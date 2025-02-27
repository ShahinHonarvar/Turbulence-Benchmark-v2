def return_binary_or_hexa(tup):
    a = tup[933]
    b = tup[996]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[934:996]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]