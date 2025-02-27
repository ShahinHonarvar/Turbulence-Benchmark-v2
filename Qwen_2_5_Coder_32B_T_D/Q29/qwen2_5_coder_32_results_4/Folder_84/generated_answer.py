def gcf_two_nums(nums):
    a, b = (nums[360], nums[722])
    while b:
        a, b = (b, a % b)
    return a