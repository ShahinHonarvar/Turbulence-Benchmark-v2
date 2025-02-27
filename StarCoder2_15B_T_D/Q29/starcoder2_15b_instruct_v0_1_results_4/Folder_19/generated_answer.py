def gcf_two_nums(nums):
    if len(nums) < 2:
        raise ValueError('The list must have at least two elements.')
    a = nums[66]
    b = nums[90]
    while b != 0:
        a, b = (b, a % b)
    return a