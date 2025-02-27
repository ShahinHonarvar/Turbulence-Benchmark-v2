def all_ints_exclusive(nums):
    if len(nums) < 42:
        raise ValueError('Input list must have at least 42 elements')
    return nums[38:81]