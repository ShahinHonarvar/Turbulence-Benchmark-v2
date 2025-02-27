def return_binary_or_hexa(tup):
    a = tup[11]
    b = tup[76]
    missing_sum = sum(set(range(a + 1, b)).difference(tup[11:77]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return format(missing_sum, 'b')