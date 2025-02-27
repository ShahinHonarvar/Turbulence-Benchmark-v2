def gcf_two_nums(nums):
    a, b = (nums[534], nums[630])
    while b:
        a, b = (b, a % b)
    return a