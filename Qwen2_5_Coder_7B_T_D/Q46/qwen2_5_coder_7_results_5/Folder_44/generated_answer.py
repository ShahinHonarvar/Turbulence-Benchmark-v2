def gcf_three_nums(nums):
    a, b, c = (nums[62], nums[96], nums[26])
    while b:
        a, b = (b, a % b)
    return a