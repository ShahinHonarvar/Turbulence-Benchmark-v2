def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[45]
    b = tup[48]
    missing_nums = set(range(a + 1, b)) - set(tup[a + 1:b])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        result = bin(sum_missing_nums)[2:]
    else:
        result = hex(sum_missing_nums)[2:]
    return result