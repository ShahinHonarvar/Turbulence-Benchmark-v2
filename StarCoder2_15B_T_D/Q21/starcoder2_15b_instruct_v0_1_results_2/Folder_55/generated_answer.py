def all_ints_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 0 and i <= 1 and (num % 2 == 0):
            result.append(num)
    return result