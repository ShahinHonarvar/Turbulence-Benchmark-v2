def gcf_three_nums(nums):
    a = nums[29]
    b = nums[53]
    c = nums[42]
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc

def gcf(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a