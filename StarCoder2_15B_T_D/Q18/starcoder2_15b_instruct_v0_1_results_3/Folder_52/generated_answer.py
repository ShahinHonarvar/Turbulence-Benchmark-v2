def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[48:60]:
        if num % 88 == 0 or num % 58 == 0:
            total += num
    return total