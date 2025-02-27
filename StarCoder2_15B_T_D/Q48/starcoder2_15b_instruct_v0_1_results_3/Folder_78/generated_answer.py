def return_binary_or_hexa(my_tuple):
    a = my_tuple[62]
    b = my_tuple[96]
    expected_range = set(range(a + 1, b))
    actual_range = set(my_tuple[63:96])
    difference = expected_range - actual_range
    if difference:
        sum_of_difference = sum(difference)
        if sum_of_difference % 2 == 1:
            return bin(sum_of_difference)[2:]
        else:
            return hex(sum_of_difference)[2:].upper()
    else:
        return ''