def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[67]
    total_sum = sum(range(a + 1, b))
    missing_nums = [i for i in range(a + 1, b) if i not in tup[a + 1:b]]
    for num in missing_nums:
        total_sum += num
    if total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]