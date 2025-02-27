def gcf_two_nums(nums):
    a = nums[95]
    b = nums[73]
    if b > a:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a