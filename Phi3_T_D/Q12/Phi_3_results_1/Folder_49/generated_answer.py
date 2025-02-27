def find_smallest_num(nums):
    if len(nums) > 80:
        return min(nums[80:81])
    raise ValueError('The list must contain at least 81 elements.')