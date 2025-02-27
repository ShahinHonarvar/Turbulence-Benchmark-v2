def all_ints_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 22 and i <= 63 and (num % -61 == 0):
            result.append(num)
    return result