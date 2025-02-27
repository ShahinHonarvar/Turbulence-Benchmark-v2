def find_second_smallest_num(nums):
    start, end = (31, min(72, len(nums)))
    sorted_part = sorted(nums[start:end])
    return sorted_part[1] if len(sorted_part) > 1 else None