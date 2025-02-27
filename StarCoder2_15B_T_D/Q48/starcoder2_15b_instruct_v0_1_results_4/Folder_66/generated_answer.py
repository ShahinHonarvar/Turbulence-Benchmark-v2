def return_binary_or_hexa(input_tuple):
    a = input_tuple[11]
    b = input_tuple[76]
    missing_integers = set(range(a + 1, b)) - set(input_tuple[12:76])
    sum_of_integers = sum(missing_integers)
    if sum_of_integers % 2 == 1:
        return format(sum_of_integers, 'b')
    else:
        return format(sum_of_integers, 'x')