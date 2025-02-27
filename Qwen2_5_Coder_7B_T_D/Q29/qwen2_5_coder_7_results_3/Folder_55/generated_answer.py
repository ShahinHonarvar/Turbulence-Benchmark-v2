def gcf_two_nums(nums):
    a, b = (nums[1], nums[2])
    while b:
        a, b = (b, a % b)
    return a