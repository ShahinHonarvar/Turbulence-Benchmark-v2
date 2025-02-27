def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[20]
    b = tuple_of_ints[93]
    missing_nums_sum = sum(set(range(a + 1, b)).difference(tuple_of_ints[20:94]))
    if missing_nums_sum % 2 == 0:
        return hex(missing_nums_sum).lstrip('0x').upper() if hex(missing_nums_sum).startswith('0') else hex(missing_nums_sum).upper()
    else:
        return bin(missing_nums_sum)[2:]