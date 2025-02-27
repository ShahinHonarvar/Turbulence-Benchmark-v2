def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    total_sum = sum(range(a + 1, b))
    missing_numbers = [x for x in range(a + 1, b) if x not in tup[13:77]]
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2 == 0:
        return format(sum_of_missing, 'x')
    else:
        return format(sum_of_missing, 'b')