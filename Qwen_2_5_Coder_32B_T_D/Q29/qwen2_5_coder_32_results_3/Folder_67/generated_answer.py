def gcf_two_nums(nums):
    a, b = (nums[64], nums[28])
    while b:
        a, b = (b, a % b)
    return a