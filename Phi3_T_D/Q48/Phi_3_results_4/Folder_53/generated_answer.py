def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[200]
    b = nums_tuple[202]
    all_nums = set(range(a + 1, b))
    present_nums = set(nums_tuple[200:203])
    missing_nums = all_nums - present_nums
    sum_missing = sum(missing_nums) if missing_nums else 0
    if sum_missing == 0:
        return ''
    elif sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]