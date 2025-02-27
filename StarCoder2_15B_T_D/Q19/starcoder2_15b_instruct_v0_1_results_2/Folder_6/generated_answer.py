def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 43 and i < 70 and (num % 69 != 0):
            result.append(num)
    return result