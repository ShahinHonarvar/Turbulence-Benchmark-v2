def gcf_two_nums(nums):
    a = nums[24]
    b = nums[68]
    while b != 0:
        a, b = (b, a % b)
    return a