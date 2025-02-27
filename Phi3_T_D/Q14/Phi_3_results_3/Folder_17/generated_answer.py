def find_second_smallest_num(nums):
    start, end = (28, min(38, len(nums)))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1] if len(sorted_slice) > 1 else None