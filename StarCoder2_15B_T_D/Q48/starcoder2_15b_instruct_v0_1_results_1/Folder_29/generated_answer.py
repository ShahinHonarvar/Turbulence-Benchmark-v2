def return_binary_or_hexa(tup: tuple) -> str:
    a = tup[70]
    b = tup[98]
    expected_nums = set(range(a + 1, b))
    actual_nums = set(tup[71:98])
    missing_nums = expected_nums - actual_nums
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()