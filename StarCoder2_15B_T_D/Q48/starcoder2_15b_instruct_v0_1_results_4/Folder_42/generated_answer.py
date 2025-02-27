def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[18]
    b = input_tuple[60]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()