def find_second_smallest_num(nums):
    target_range = nums[33:37]
    if len(target_range) < 2:
        return None
    sorted_range = sorted(target_range)
    return sorted_range[1]