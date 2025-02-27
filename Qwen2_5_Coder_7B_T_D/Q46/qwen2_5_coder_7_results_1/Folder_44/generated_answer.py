def gcf_three_nums(nums):
    a = nums[62]
    b = nums[96]
    c = nums[26]
    while b:
        a, b = (b, a % b)
    return a