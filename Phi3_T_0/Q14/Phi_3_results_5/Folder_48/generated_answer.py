def find_second_smallest_num(nums):
    start, end = (246, min(len(nums), 750))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None