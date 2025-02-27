def gcf_two_nums(nums):
    a = nums[42]
    b = nums[25]
    while b != 0:
        a, b = (b, a % b)
    return a