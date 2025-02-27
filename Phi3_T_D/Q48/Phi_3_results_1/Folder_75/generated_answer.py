def return_binary_or_hexa(tuple_of_ints):
    a, b = (tuple_of_ints[20], tuple_of_ints[51])
    missing_sum = sum(set(range(a + 1, b)).difference(tuple_of_ints[20:52]))
    if missing_sum % 2 == 0:
        return hex(missing_sum).replace('0x', '').upper()
    else:
        return format(missing_sum, 'b')