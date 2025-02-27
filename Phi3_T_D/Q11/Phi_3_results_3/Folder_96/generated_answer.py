def find_largest_num(nums):
    if len(nums) < 201:
        raise ValueError('List must contain at least 201 elements.')
    return max(nums[50:201])