def gcf_two_nums(nums):
    a, b = (nums[372], nums[752])
    while b:
        a, b = (b, a % b)
    return a