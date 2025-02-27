def return_binary_or_hexa(input_tuple):
    a = input_tuple[70]
    b = input_tuple[98]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    elif sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    else:
        return ''