def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    missing_sum = sum((i for i in range(a + 1, b) if i not in t[1:3]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x').upper()