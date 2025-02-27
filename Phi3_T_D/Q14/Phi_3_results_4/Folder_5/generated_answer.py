def find_second_smallest_num(nums):
    start, end = (3, min(len(nums), 6))
    if start >= end:
        return None
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1] if len(sorted_slice) > 1 else None