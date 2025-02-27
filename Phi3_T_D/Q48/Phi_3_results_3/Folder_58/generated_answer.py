def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[275], int_tuple[871])
    needed_numbers = set(range(a + 1, b))
    present_numbers = set(int_tuple[275:872])
    sum_missing_numbers = sum(needed_numbers - present_numbers)
    if sum_missing_numbers % 2 == 0:
        return '{:x}'.format(sum_missing_numbers)
    else:
        return '{:b}'.format(sum_missing_numbers)[2:]