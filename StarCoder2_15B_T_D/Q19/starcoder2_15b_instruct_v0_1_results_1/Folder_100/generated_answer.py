def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 62 and i < 96 and (num % 26 != 0):
            result.append(num)
    return result