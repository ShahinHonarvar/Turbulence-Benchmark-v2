def return_binary_or_hexa(ints):
    a = ints[11]
    b = ints[76]
    range_sum = sum(range(a + 1, b))
    missing_sum = sum((x for x in range(a + 1, b) if x not in ints[11:76]))
    if missing_sum > 0:
        if missing_sum % 2 == 1:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:]
    else:
        return ''