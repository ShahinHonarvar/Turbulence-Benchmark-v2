def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    missing_ints = []
    for i in range(a + 1, b):
        if i not in tup:
            missing_ints.append(i)
    sum_of_missing_ints = sum(missing_ints)
    if sum_of_missing_ints % 2 == 0:
        return format(sum_of_missing_ints, 'x')
    else:
        return format(sum_of_missing_ints, 'b')