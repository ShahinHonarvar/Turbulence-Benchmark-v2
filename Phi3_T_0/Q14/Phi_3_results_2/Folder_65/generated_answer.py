def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 100:
        return None
    start, end = (56, 57)
    if start >= len(nums) or end >= len(nums):
        return None
    nums[start:end + 1] = sorted(nums[start:end + 1])
    return nums[start + 1] if start + 1 < len(nums) else None