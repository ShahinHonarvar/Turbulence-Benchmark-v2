def gcf_two_nums(nums):
    a = nums[90]
    b = nums[54]
    if a < b:
        a, b = (b, a)
    while b != 0:
        a, b = (b, a % b)
    return a