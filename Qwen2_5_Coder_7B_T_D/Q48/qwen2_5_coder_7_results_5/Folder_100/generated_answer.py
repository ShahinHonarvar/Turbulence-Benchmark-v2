def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    required_range = set(range(a + 1, b))
    present_in_tuple = set(t[44:79])
    missing_numbers = required_range - present_in_tuple
    if missing_numbers:
        sum_missing = sum(missing_numbers)
        if sum_missing % 2 == 0:
            return format(sum_missing, 'x')
        else:
            return format(sum_missing, 'b')
    else:
        return ''