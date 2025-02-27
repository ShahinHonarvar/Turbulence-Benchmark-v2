def gcf_two_nums(nums):
    a, b = (nums[84], nums[63])
    while b:
        a, b = (b, a % b)
    return a