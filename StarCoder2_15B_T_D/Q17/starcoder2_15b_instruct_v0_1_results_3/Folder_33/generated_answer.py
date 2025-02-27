def all_ints_div_by_both_two_nums(nums):
    res = []
    for i, num in enumerate(nums):
        if i >= 281 and i <= 694 and (num % -722 == 0) and (num % -731 == 0):
            res.append(num)
    return res