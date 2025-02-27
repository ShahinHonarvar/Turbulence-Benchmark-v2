def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    required_sum = sum(range(a + 1, b)) - sum((x for x in t if a < x < b))
    if required_sum % 2 == 0:
        return format(required_sum, 'x')
    else:
        return format(required_sum, 'b')