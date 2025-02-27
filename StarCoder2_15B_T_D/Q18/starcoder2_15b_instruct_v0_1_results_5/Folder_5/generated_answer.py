def sum_ints_div_by_either_nums(nums):
    result = 0
    for num in nums[0:2]:
        if num % -6 == 0 or num % 4 == 0:
            result += num
    return result