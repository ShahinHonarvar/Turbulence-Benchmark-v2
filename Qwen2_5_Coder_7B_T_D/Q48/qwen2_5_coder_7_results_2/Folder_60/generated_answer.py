def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    total_sum = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in tup[a + 1:b]]
    for i in missing:
        total_sum -= i
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')