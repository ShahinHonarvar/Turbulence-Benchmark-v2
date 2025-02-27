def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[1]
    b = tuple_of_ints[7]
    sum_of_ints = sum(range(a + 1, b))
    for i in tuple_of_ints:
        if i > a and i < b:
            sum_of_ints -= i
    if sum_of_ints % 2 == 1:
        return bin(sum_of_ints)[2:]
    else:
        return hex(sum_of_ints)[2:].upper()