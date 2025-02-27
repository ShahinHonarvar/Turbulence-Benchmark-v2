def find_largest_num(nums):
    if not 75 <= len(nums) <= 94:
        raise ValueError('List must contain at least 75 elements and at most 94 elements')
    return max(nums[75:95])