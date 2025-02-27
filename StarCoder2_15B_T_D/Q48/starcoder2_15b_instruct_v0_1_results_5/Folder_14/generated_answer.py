def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[2]
    b = input_tuple[5]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple[2:5]:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return format(sum_of_integers, 'b')
    else:
        return format(sum_of_integers, 'x')