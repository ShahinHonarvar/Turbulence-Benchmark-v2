def gcf_two_nums(nums):
    if len(nums) < 79 or len(nums) < 17:
        raise ValueError('List must have at least 79 and 17 elements')
    a = nums[78]
    b = nums[16]
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a