def gcf_two_nums(nums):
    a, b = (nums[85], nums[51])
    while b:
        a, b = (b, a % b)
    return a