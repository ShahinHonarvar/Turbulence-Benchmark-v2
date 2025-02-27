def gcf_two_nums(nums):
    gcf = nums[28]
    for i in range(29, 50):
        gcf = gcf_two_nums_helper(gcf, nums[i])
    return gcf

def gcf_two_nums_helper(n1, n2):
    while n2 != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    return n1