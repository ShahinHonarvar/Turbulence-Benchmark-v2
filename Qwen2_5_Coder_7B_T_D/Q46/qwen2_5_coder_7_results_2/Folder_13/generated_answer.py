def gcf_three_nums(nums):
    a = nums[991]
    b = nums[244]
    c = nums[974]
    while b:
        a, b = (b, a % b)
    return a