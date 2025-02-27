def gcf_three_nums(nums):
    a, b, c = (nums[59], nums[93], nums[84])
    while b:
        a, b = (b, a % b)
    return a