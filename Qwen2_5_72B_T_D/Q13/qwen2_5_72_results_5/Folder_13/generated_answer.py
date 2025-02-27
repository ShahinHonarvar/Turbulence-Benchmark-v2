def find_second_largest_num(nums):
    if len(nums) < 88 or len(nums) < 26:
        return None
    segment = nums[25:88]
    if len(segment) < 2:
        return None
    segment.sort()
    return segment[-2] if len(segment) > 1 else None