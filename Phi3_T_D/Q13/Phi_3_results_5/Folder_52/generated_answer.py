def find_second_largest_num(nums):
    segment = nums[28:39]
    if len(segment) < 1:
        return None
    else:
        segment.sort()
        return segment[-2] if len(segment) > 1 else None