def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[86]
    b = input_tuple[90]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return format(sum_of_integers, 'b')
    else:
        return format(sum_of_integers, 'x')