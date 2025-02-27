def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 100:
        return None
    start, end = (56, 57)
    if start < 0 or end >= len(nums) or start > end:
        return None
    nums = sorted(nums[start:end + 1], reverse=True)
    return nums[1] if len(nums) > 1 else None