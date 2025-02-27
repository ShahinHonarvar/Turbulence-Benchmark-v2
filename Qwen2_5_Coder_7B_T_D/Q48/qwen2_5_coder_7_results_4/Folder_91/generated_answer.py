def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[6])
    total_sum = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(tup[1:7])
    for num in missing_nums:
        total_sum += num
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()