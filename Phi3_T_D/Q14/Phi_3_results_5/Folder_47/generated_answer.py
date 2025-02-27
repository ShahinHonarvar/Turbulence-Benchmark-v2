def find_second_smallest_num(nums):
    valid_range = nums[22:64]
    unique_sorted = sorted(set(valid_range))
    return unique_sorted[1] if len(unique_sorted) > 1 else None