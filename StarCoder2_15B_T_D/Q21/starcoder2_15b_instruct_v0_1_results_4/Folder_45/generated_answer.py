def all_ints_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 0 and i <= 2 and (num % 9 == 0):
            result.append(num)
    return result