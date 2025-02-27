def find_second_smallest_num(nums):
    target_range = nums[40:201]
    if len(target_range) < 2:
        return None
    return sorted(target_range)[1]