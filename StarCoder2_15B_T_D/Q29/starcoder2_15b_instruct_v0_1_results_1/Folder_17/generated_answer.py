def gcf_two_nums(nums):
    a = nums[69]
    b = nums[40]
    while b != 0:
        a, b = (b, a % b)
    return a