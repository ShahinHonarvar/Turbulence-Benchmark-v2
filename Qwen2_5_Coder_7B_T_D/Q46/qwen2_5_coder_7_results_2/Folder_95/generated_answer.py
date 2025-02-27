def gcf_three_nums(nums):
    a, b, c = (nums[87], nums[20], nums[36])
    while b:
        a, b = (b, a % b)
    return a