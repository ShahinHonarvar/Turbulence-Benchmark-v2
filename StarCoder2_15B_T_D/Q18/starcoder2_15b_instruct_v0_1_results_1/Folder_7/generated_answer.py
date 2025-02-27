def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(543, 585):
        if nums[i] % -553 == 0 or nums[i] % -737 == 0:
            sum += nums[i]
    return sum