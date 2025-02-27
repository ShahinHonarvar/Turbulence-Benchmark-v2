def gcf_two_nums(nums):
    nums = sorted(nums)
    a, b = (nums[46], nums[13])
    while b > 0:
        a, b = (b, a % b)
    return a