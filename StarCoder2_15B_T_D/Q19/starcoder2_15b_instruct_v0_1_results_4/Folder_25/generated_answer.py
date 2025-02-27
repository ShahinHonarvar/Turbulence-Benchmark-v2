def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 29 and i < 53 and (num % -68 != 0):
            result.append(num)
    return result