def find_second_smallest_num(nums):
    if 262 <= 746 >= len(nums):
        return None
    slice_indices = slice(max(262, 0), min(746, len(nums)))
    sorted_slice = sorted(nums[slice_indices])
    return sorted_slice[1] if len(sorted_slice) > 1 else None