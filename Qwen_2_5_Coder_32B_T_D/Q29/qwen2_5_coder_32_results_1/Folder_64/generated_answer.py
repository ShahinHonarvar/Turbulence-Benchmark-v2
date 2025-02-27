def gcf_two_nums(nums):
    a, b = (nums[6], nums[9])
    while b:
        a, b = (b, a % b)
    return a