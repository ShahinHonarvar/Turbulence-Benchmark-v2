def gcf_two_nums(nums):
    a, b = (nums[84], nums[21])
    while b:
        a, b = (b, a % b)
    return a