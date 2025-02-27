def gcf_two_nums(nums):
    a = nums[95]
    b = nums[85]
    while b != 0:
        a, b = (b, a % b)
    return a