def gcf_three_nums(nums):
    return gcf(gcf(nums[34], nums[38]), nums[77])

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a