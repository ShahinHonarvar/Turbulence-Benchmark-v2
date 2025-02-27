def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[7]
    total_sum = sum(range(a + 1, b))
    missing_numbers = set(range(a + 1, b)) - set(tup[a:b + 1])
    for num in missing_numbers:
        total_sum += num
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')