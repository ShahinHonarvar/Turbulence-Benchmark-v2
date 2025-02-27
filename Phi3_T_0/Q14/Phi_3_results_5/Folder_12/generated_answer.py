def find_second_smallest_num(nums):
    start, end = (31, 72)
    if start > end or end >= len(nums):
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None