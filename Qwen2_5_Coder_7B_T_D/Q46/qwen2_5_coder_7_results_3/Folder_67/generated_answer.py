def gcf_three_nums(nums):
    a = nums[70]
    b = nums[41]
    c = nums[20]
    while b != 0:
        a, b = (b, a % b)
    return a