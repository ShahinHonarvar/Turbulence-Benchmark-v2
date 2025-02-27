def return_binary_or_hexa(tup):
    missing_sum = sum(set(range(tup[9][0] + 1, tup[96][0])).difference(tup[9:97]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')