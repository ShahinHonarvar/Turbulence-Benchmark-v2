def gcf_three_nums(nums):
    nums = sorted(nums)
    a, b, c = (nums[18], nums[10], nums[76])
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a