def gcf_two_nums(nums):
    if len(nums) < 91:
        raise IndexError('List length should be at least 91')
    a = nums[66]
    b = nums[90]
    while b != 0:
        a, b = (b, a % b)
    return a