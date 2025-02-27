def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[9]
    total_sum = sum(range(a + 1, b))
    missing = set(range(a + 1, b)) - set(tup[1:9])
    for num in missing:
        total_sum -= num
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')