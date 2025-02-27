def gcf_three_nums(nums):
    gcf = nums[53]
    for i in range(53, 45, -1):
        if i == 53:
            continue
        gcf = gcf_two_nums(gcf, nums[i])
    return gcf

def gcf_two_nums(a, b):
    if a == 0:
        return b
    return gcf_two_nums(b % a, a)