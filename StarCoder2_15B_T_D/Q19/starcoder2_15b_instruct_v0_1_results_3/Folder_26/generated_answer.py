def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 38 and i < 81 and (num % 49 != 0):
            result.append(num)
    return result