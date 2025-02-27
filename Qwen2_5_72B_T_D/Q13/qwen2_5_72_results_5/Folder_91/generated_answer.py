def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    segment = nums[:6]
    segment.sort()
    if len(set(segment)) < 2:
        return None
    return segment[-2]