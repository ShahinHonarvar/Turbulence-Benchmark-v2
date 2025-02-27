def gcf_two_nums(nums):
    a, b = (nums[83], nums[14])
    while b:
        a, b = (b, a % b)
    return a