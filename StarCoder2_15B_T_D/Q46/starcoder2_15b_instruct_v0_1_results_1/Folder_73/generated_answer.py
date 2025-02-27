def gcf_three_nums(nums):
    gcf_90_84 = nums[90]
    for i in range(90, 84, -1):
        gcf_90_84 = gcf(gcf_90_84, nums[i - 1])
    gcf_90_84_47 = gcf_90_84
    for i in range(84, 47, -1):
        gcf_90_84_47 = gcf(gcf_90_84_47, nums[i - 1])
    return gcf_90_84_47

def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a