def return_binary_or_hexa(input_tuple):
    a = input_tuple[36]
    b = input_tuple[52]
    missing_integers = set(range(a + 1, b)) - set(input_tuple[a + 1:b])
    if missing_integers:
        sum_of_missing_integers = sum(missing_integers)
        if sum_of_missing_integers % 2 == 1:
            return bin(sum_of_missing_integers)[2:]
        else:
            return hex(sum_of_missing_integers)[2:]
    else:
        return ''