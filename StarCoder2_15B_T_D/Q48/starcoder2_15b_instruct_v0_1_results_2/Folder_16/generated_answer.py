def return_binary_or_hexa(my_tuple):
    a = my_tuple[90]
    b = my_tuple[97]
    missing_ints = set(range(a + 1, b)) - set(my_tuple[a + 1:b])
    sum_missing_ints = sum(missing_ints)
    if sum_missing_ints % 2 == 1:
        return bin(sum_missing_ints)[2:]
    else:
        return hex(sum_missing_ints)[2:].upper() if sum_missing_ints != 0 else ''