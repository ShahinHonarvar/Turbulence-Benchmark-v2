def all_ints_div_by_both_two_nums(nums):
    result = []
    for i, num in enumerate(nums):
        if num % 31 == 0 and num % 11 == 0 and (61 <= i <= 88):
            result.append(num)
    return result