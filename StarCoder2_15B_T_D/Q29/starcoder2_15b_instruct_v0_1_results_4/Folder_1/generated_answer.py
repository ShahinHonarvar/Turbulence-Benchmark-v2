def gcf_two_nums(nums):
    a = nums[13]
    b = nums[66]
    if a > b:
        a, b = (b, a)
    if a == 0:
        return b
    return gcf_two_nums([a, b - a])