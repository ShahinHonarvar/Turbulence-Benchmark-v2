def gcf_two_nums(nums):
    a = nums[27]
    b = nums[48]
    while b:
        a, b = (b, a % b)
    return a