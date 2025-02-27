def all_ints_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 10 and i <= 52 and (num % -12 == 0):
            result.append(num)
    return result