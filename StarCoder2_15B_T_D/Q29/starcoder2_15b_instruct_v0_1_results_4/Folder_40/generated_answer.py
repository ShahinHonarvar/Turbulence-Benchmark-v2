def gcf_two_nums(nums):
    if len(nums) < 10:
        return None
    a = nums[7]
    b = nums[9]
    while b != 0:
        a, b = (b, a % b)
    return a