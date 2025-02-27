def gcf_three_nums(nums):
    a, b, c = (nums[92], nums[69], nums[95])
    while b:
        a, b = (b, a % b)
    return a