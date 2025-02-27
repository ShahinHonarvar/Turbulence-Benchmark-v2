def return_binary_or_hexa(my_tuple):
    a = my_tuple[86]
    b = my_tuple[89]
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in my_tuple:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    elif sum_of_integers > 0:
        return hex(sum_of_integers)[2:]
    else:
        return ''