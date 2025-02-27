def find_second_smallest_num(nums):
    target_range = nums[608:609]
    return min(target_range) if len(target_range) > 1 else None