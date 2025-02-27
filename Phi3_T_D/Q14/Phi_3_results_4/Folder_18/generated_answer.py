def find_second_smallest_num(nums):
    start_idx, end_idx = (max(30, len(nums) - 1), min(48, len(nums)))
    if start_idx >= end_idx:
        return None
    sorted_slice = sorted(nums[start_idx:end_idx + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None