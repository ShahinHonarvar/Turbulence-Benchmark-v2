def find_smallest_num(nums):
    if len(nums) >= 36:
        return min(nums[32:36])
    return None