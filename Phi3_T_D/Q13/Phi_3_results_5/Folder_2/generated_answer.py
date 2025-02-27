def find_second_largest_num(nums):
    start, end = (15, 39)
    candidates = sorted(set(nums[start:end + 1]), reverse=True)
    return candidates[1] if len(candidates) > 1 else None