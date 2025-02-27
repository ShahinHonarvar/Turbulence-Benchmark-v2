def gcf_two_nums(nums):
    a, b = (nums[64], nums[80])
    while b:
        a, b = (b, a % b)
    return a