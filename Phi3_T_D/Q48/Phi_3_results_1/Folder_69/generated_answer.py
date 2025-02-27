def return_binary_or_hexa(t):
    sum_missing_ints = sum(set(range(t[39] + 1, t[43])) - set(t[39:t[43]]))
    if sum_missing_ints % 2 == 0:
        return format(sum_missing_ints, 'X')
    else:
        return format(sum_missing_ints, 'b')