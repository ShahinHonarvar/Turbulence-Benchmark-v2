def find_smallest_num(nums):
    return min(nums[70:201], default=None) if len(nums) > 200 else None