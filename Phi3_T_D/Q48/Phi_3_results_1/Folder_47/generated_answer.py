def return_binary_or_hexa(input_tuple):
    a = input_tuple[29]
    b = input_tuple[53]
    sum_not_present = sum(set(range(a + 1, b)).difference(input_tuple[29:54]))
    if sum_not_present % 2 == 0:
        return hex(sum_not_present)[2:]
    else:
        return bin(sum_not_present)[2:]