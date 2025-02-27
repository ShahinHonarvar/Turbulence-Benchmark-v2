def gcf_two_nums(nums):
    a, b = (nums[841], nums[804])
    while b:
        a, b = (b, a % b)
    return a