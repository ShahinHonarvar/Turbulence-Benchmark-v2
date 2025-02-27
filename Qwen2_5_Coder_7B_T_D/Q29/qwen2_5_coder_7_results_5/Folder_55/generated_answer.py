def gcf_two_nums(nums):
    a = nums[1]
    b = nums[2]
    while b:
        a, b = (b, a % b)
    return a