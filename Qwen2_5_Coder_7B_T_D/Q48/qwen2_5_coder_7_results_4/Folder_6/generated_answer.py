def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[93]
    total_sum = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(tup[a + 1:b])
    for num in missing_nums:
        total_sum += num
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return bin(total_sum)[2:]