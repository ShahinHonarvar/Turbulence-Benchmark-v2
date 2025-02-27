def find_largest_num(nums):
    if len(nums) < 86:
        raise ValueError('List must contain at least 86 elements')
    return max(nums[75:86])