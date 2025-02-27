def all_ints_not_div_by_num(nums):
    res = []
    for i, num in enumerate(nums):
        if i >= 3 and i < 9 and (num % 6 != 0):
            res.append(num)
    return res