def gcf_two_nums(nums):
    a, b = (nums[91], nums[45])
    while b:
        a, b = (b, a % b)
    return a