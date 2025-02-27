def gcf_three_nums(nums):
    return gcf(nums[0], nums[8], nums[3])

def gcf(a, b, c):
    smaller = min(a, b, c)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1