def all_ints_div_by_both_two_nums(nums):
    result = []
    for i, num in enumerate(nums):
        if num % 39 == 0 and num % 15 == 0 and (44 <= i <= 59):
            result.append(num)
    return result