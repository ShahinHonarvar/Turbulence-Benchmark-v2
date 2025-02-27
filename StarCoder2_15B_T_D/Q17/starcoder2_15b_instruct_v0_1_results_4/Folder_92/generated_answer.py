def all_ints_div_by_both_two_nums(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 0 and i <= 0 and (num % 1 == 0) and (num % -1 == 0):
            result.append(num)
    return result