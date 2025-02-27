def find_second_largest_num(nums):
    start, end = (74, min(len(nums), 95))
    sorted_range = sorted(nums[start:end + 1], reverse=True)
    return sorted_range[1] if len(sorted_range) > 1 else None