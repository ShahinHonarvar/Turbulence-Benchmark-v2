def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[46]
    b = tup[91]
    missing_values = set(range(a + 1, b)) - set(tup[46:91])
    sum_of_missing_values = sum(missing_values)
    if sum_of_missing_values % 2 == 1:
        return bin(sum_of_missing_values)[2:]
    else:
        return hex(sum_of_missing_values)[2:].upper()