def find_second_smallest_num(nums):
    start, end = (527, 538)
    if start > end or start < 0 or end >= len(nums):
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None