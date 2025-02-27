def return_binary_or_hexa(input_tuple):
    a = input_tuple[10]
    b = input_tuple[12]
    sum_of_ints = sum(range(a + 1, b))
    if sum_of_ints % 2 == 1:
        return bin(sum_of_ints)[2:]
    else:
        return hex(sum_of_ints)[2:].upper()