def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 15 and i < 20 and (num % 93 != 0):
            result.append(num)
    return result