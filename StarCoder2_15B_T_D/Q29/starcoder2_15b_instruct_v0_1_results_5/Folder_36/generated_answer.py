def gcf_two_nums(nums):
    a = nums[429]
    b = nums[289]
    while b != 0:
        a, b = (b, a % b)
    return a