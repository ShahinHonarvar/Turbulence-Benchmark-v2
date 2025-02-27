def gcf_three_nums(nums):
    gcf = nums[85]
    for i in range(86, 54, -1):
        gcf = gcf_two_nums(gcf, nums[i])
    for i in range(53, 36, -1):
        gcf = gcf_two_nums(gcf, nums[i])
    return gcf

def gcf_two_nums(a, b):
    if a == 0:
        return b
    return gcf_two_nums(b % a, a)