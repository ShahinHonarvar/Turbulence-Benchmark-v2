def return_binary_or_hexa(input_tuple):
    a = input_tuple[43]
    b = input_tuple[70]
    sum_of_missing_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_missing_integers += i
    if sum_of_missing_integers % 2 == 1:
        output = format(sum_of_missing_integers, 'b')
    else:
        output = format(sum_of_missing_integers, 'x')
    return output