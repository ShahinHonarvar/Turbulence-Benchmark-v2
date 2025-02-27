def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[2]
    b = tuple_of_ints[8]
    sum_of_missing_ints = 0
    for i in range(a + 1, b):
        if i not in tuple_of_ints[2:8]:
            sum_of_missing_ints += i
    if sum_of_missing_ints % 2 == 1:
        return bin(sum_of_missing_ints)[2:]
    else:
        return hex(sum_of_missing_ints)[2:]