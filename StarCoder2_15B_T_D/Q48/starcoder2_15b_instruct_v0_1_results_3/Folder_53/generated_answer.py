def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[200]
    b = tup[202]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in tup:
            missing_nums.append(num)
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper() if sum_missing_nums != 0 else ''