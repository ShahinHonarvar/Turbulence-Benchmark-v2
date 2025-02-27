def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[3]
    b = numbers_tuple[8]
    integers = set(range(a + 1, b))
    sum_of_integers = sum(integers - set(numbers_tuple[3:9]))
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()