def find_second_smallest_num(nums):
    if len(nums) - 30 < 88:
        return None
    segment = sorted(nums[30:88])
    return segment[1] if len(segment) > 1 else None