def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[13:77]))
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')