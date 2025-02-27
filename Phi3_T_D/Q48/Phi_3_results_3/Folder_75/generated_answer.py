def return_binary_or_hexa(ints):
    a, b = (ints[20], ints[51])
    missing_sum = sum((i for i in range(a + 1, b, 1) if i not in ints[20:52])) - (a + 1)
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x').upper()
    else:
        return format(missing_sum, 'b')