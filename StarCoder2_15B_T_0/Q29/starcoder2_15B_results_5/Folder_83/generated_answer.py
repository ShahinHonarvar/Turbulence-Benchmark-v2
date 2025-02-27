def gcf_two_nums(nums):
    if len(nums) < 21:
        raise ValueError('List must have at least 21 elements')
    a = nums[17]
    b = nums[20]
    while b != 0:
        a, b = (b, a % b)
    return a