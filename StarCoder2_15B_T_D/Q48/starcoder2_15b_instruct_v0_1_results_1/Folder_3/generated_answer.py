def return_binary_or_hexa(given_tuple):
    a = given_tuple[56]
    b = given_tuple[88]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in given_tuple:
            sum_of_integers += i
    if sum_of_integers == 0:
        return ''
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()