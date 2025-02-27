def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[8])
    present_nums = set(tup[1:9])
    sum_nums = sum((i for i in range(a + 1, b) if i not in present_nums))
    if sum_nums % 2 == 0:
        result = hex(sum_nums)[2:]
    else:
        result = bin(sum_nums)[2:]
    return result