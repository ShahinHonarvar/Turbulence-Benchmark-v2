def find_second_smallest_num(nums):
    start, end = (10, 66)
    if end >= len(nums):
        end = len(nums) - 1
    sorted_segment = sorted(nums[start:end + 1])
    return sorted_segment[1] if len(sorted_segment) > 1 else None