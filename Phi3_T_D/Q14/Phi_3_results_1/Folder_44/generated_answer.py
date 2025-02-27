def find_second_smallest_num(nums):
    start, end = (91, 99)
    if len(nums) < end + 1 or start >= len(nums):
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None