def gcf_two_nums(nums):
    a = nums[38]
    b = nums[77]
    while b != 0:
        a, b = (b, a % b)
    return a