def find_smallest_num(nums):
    if not isinstance(nums, list) or len(nums) < 14:
        raise ValueError('Invalid list or list length is less than 14.')
    sub_list = nums[527:539]
    return min(sub_list)