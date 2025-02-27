def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[90]
    total_sum = sum(range(a + 1, b))
    present_nums = set(tup[86:91])
    missing_nums = [num for num in range(a + 1, b) if num not in present_nums]
    sum_of_missing = sum(missing_nums)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()