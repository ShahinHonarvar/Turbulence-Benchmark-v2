def return_binary_or_hexa(input_tuple):
    a = input_tuple[0]
    b = input_tuple[5]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].rstrip('L')
    else:
        return bin(sum_of_integers)[2:]