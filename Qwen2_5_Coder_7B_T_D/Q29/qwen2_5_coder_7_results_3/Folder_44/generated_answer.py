def gcf_two_nums(nums):
    a, b = (nums[56], nums[88])
    while b:
        a, b = (b, a % b)
    return a