def all_ints_not_div_by_num(nums):
    res = []
    for i, num in enumerate(nums):
        if num % 26 != 0 and 62 <= i < 96:
            res.append(num)
    return res