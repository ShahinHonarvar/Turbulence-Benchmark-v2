def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[0:2]:
        if num % -6 == 0 and num % 4 == 0:
            result.append(num)
    return result