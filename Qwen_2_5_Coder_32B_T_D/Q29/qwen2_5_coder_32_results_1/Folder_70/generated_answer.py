def gcf_two_nums(nums):
    a, b = (nums[300], nums[616])
    while b:
        a, b = (b, a % b)
    return a