def gcf_two_nums(nums):
    a = nums[19]
    b = nums[94]
    while b:
        a, b = (b, a % b)
    return a