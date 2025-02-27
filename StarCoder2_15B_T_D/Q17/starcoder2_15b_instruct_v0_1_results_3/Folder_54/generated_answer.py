def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums:
        if num % -65 == 0 and num % -62 == 0:
            result.append(num)
    return result