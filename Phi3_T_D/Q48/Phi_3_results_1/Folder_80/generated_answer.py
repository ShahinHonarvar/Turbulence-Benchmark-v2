def return_binary_or_hexa(num_tuple):
    a = num_tuple[57]
    b = num_tuple[84]
    absent_sum = sum((x for x in range(a + 1, b) if x not in num_tuple[57:84 + 1]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:].upper()
    else:
        return bin(absent_sum)[2:]