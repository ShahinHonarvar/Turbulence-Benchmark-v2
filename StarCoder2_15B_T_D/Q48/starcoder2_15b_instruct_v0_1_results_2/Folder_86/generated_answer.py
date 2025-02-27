def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[19]
    b = tup[32]
    missing_nums = set(range(a + 1, b)) - set(tup[19:33])
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:]