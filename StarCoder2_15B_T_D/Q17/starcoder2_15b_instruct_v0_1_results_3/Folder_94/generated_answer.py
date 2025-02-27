def all_ints_div_by_both_two_nums(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 93 and i <= 94 and (num % -53 == 0) and (num % -91 == 0):
            result.append(num)
    return result