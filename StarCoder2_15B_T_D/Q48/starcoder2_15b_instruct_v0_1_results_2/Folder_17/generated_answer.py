def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[73], input_tuple[84])
    missing_ints = set(range(a + 1, b)) - set(input_tuple[73:85])
    sum_of_missing_ints = sum(missing_ints)
    if sum_of_missing_ints % 2 == 1:
        return bin(sum_of_missing_ints)[2:]
    else:
        return hex(sum_of_missing_ints)[2:].upper()