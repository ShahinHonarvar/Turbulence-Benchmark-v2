def gcf_three_nums(nums):
    a, b, c = (nums[90], nums[54], nums[96])
    smaller = min(a, b, c)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1