def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 8 and i < 9 and (num % 8 != 0):
            result.append(num)
    return result