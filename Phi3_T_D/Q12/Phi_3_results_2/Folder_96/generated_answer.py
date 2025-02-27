def find_smallest_num(nums):
    if len(nums) < 201:
        raise ValueError('List must have at least 201 elements')
    return min(nums[50:201])