def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[20]
    b = tuple_of_ints[36]
    sum_of_ints = 0
    for i in range(a + 1, b):
        if i not in tuple_of_ints[20:37]:
            sum_of_ints += i
    if sum_of_ints % 2 == 1:
        return bin(sum_of_ints)[2:]
    else:
        return hex(sum_of_ints)[2:]