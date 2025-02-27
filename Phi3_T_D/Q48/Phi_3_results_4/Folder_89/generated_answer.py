def return_binary_or_hexa(tu):
    a, b = (tu[55], tu[84])
    missing_sum = sum(set(range(a + 1, b)) - set(tu[55:85]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return format(missing_sum, 'x')