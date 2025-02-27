def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 20 and i < 50 and (num % 40 != 0):
            result.append(num)
    return result