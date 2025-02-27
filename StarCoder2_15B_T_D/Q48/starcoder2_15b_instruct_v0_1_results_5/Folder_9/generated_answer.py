def return_binary_or_hexa(arg):
    tuple_of_ints = arg[0]
    a = tuple_of_ints[70]
    b = tuple_of_ints[200]
    sum_of_ints = 0
    for i in range(a + 1, b):
        if i not in tuple_of_ints[70:200]:
            sum_of_ints += i
    if sum_of_ints % 2 == 1:
        return bin(sum_of_ints)[2:]
    else:
        return hex(sum_of_ints)[2:].upper()