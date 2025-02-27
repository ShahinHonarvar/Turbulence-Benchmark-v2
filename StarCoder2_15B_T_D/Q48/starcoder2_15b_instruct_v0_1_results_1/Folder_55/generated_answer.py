def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    missing_nums = set(range(a + 1, b)) - set(tup[a + 1:b])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()