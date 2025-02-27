def all_ints_div_by_both_two_nums(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 44 and i <= 59 and (num % 39 == 0) and (num % 15 == 0):
            result.append(num)
    return result