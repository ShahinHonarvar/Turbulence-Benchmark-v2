def return_binary_or_hexa(e_tuple):
    a = e_tuple[62]
    b = e_tuple[96]
    missing_sum = sum((x for x in range(a + 1, b) if x not in e_tuple[62:96 + 1]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]