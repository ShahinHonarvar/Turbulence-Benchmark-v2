def all_ints_not_div_by_num(nums):
    res = []
    for i, num in enumerate(nums):
        if i >= 15 and i < 57 and (num % 86 != 0):
            res.append(num)
    return res