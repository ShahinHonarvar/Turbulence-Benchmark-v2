def gcf_three_nums(nums):
    a, b, c = (nums[693], nums[331], nums[668])
    while b:
        a, b = (b, a % b)
    return a