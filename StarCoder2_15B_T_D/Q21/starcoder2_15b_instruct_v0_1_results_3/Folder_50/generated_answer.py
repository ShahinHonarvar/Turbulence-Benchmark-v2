def all_ints_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 36 and i <= 46 and (num % 28 == 0):
            result.append(num)
    return result