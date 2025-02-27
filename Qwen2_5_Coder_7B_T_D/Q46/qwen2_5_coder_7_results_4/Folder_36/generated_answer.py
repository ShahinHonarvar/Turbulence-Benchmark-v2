def gcf_three_nums(nums):
    a, b, c = (nums[427], nums[761], nums[148])
    while b:
        a, b = (b, a % b)
    return a