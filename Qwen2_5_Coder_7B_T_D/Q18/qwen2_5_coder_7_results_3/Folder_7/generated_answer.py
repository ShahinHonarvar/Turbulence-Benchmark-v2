def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(543, 585):
        if nums[i] % -553 == 0 or nums[i] % -737 == 0:
            total += nums[i]
    return total