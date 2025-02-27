def gcf_two_nums(nums):
    a, b = (nums[166], nums[106])
    while b:
        a, b = (b, a % b)
    return a