def find_second_smallest_num(nums):
    start, end = (42, 68)
    if end >= len(nums):
        end = len(nums) - 1
    if start >= end:
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None