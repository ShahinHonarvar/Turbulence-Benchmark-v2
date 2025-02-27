def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[58:76]:
        if num % 72 == 0 or num % 62 == 0:
            total += num
    return total