def find_second_smallest_num(nums):
    start, end = (68, 86)
    if start >= end or end > len(nums):
        return None
    subset = sorted(nums[start:end + 1])
    return subset[1] if len(subset) > 1 else None