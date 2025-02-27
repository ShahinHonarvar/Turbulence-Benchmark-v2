def gcf_three_nums(nums):
    return gcf(nums[59], gcf(nums[93], nums[84]))

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a