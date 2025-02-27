def gcf_two_nums(nums):
    a, b = (nums[51], nums[27])
    while b:
        a, b = (b, a % b)
    return a