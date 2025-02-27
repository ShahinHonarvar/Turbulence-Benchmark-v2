def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[10]
    b = tuple_of_ints[12]
    missing_sum = sum((x for x in range(a + 1, b) if x not in tuple_of_ints[10:12]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]