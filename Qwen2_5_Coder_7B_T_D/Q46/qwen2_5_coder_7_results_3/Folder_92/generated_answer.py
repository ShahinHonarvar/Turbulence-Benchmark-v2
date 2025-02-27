def gcf_three_nums(nums):
    a, b, c = (nums[0], nums[7], nums[9])
    while b:
        a, b = (b, a % b)
    return a