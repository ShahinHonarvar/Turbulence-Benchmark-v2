def return_binary_or_hexa(tuple_ints):
    a = tuple_ints[3]
    b = tuple_ints[8]
    missing_sum = sum((i for i in range(a + 1, b) if i not in tuple_ints[3:9]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]