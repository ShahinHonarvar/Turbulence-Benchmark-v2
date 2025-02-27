def find_second_smallest_num(nums):
    start, end = (min(42, len(nums)), min(68, len(nums)))
    return sorted(nums[start:end + 1])[1] if len(nums[start:end + 1]) >= 2 else None