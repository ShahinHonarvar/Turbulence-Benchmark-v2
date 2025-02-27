def gcf_two_nums(nums):
    a = nums[0]
    b = nums[4]
    while b:
        a, b = (b, a % b)
    return a