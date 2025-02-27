def find_smallest_num(nums):
    if len(nums) < 40:
        raise ValueError('List must contain at least 100 elements.')
    return min(nums[62:99])