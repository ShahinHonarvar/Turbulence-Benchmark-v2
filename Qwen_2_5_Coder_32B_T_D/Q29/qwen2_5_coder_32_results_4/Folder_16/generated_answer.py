def gcf_two_nums(nums):
    a, b = (nums[860], nums[307])
    while b:
        a, b = (b, a % b)
    return a