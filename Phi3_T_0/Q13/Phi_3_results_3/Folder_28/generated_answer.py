def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    start, end = (62, 63)
    if start > end or end >= len(nums):
        return None
    return sorted(nums[start:end + 1])[-2]