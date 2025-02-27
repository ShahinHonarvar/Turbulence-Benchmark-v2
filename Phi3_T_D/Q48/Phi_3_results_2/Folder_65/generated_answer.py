def return_binary_or_hexa(int_tuple):
    a = int_tuple[51] + 1
    b = int_tuple[76] - 1
    missing_nums = set(range(a, b + 1)) - set(int_tuple[51:77])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 != 0:
        return format(sum_missing, '0b')
    else:
        return '{:x}'.format(sum_missing)