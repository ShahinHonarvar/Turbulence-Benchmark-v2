def return_binary_or_hexa(my_tuple: tuple) -> str:
    a, b = (my_tuple[68], my_tuple[99])
    sum_of_integers = 0
    for i in range(a + 1, b):
        if i not in my_tuple[68:100]:
            sum_of_integers += i
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()