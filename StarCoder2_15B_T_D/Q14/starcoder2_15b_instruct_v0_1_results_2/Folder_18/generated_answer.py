def find_second_smallest_num(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        raise ValueError('Invalid input list')
    nums.sort()
    if len(nums) > 48:
        return nums[31]
    return None