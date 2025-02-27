def find_second_smallest_num(nums):
    valid_range = nums[29:94]
    if len(valid_range) < 2:
        return None
    sorted_range = sorted(valid_range)
    return sorted_range[1]