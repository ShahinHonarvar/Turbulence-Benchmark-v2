def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[20]
    b = input_tuple[200]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].rstrip('L')
    else:
        return bin(sum_of_integers)[2:]