def gcf_two_nums(nums):
    a = nums[28]
    b = nums[17]
    while b != 0:
        a, b = (b, a % b)
    return a