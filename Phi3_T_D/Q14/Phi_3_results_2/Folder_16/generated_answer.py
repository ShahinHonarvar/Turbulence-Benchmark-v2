def find_second_smallest_num(nums):
    start, end = (66, min(77, len(nums)))
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1] if len(sorted_slice) > 1 else None