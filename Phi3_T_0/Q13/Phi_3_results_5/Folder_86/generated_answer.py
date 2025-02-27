def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    start, end = (31, 34)
    return sorted(nums[start:end + 1])[-2] if len(nums[start:end + 1]) > 1 else None