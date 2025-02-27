def find_second_smallest_num(nums):
    start, end = (4, min(len(nums), 9))
    if end - start < 5:
        return None
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1] if len(sorted_slice) > 1 else None