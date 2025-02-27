def find_second_smallest_num(nums):
    start, end = (max(661, len(nums)), min(924, len(nums)))
    if end - start < 3:
        return None
    unique_sorted_slice = sorted(set(nums[start:end + 1]))
    return unique_sorted_slice[1] if len(unique_sorted_slice) >= 2 else None