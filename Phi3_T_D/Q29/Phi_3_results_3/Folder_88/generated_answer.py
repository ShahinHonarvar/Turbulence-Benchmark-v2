def gcf_two_nums(nums):
    a, b = (nums[27], nums[34])
    while b:
        a, b = (b, a % b)
    return a