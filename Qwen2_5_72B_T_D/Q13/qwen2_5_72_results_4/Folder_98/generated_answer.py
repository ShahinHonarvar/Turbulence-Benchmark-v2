def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    segment = nums[:7]
    segment.sort()
    if len(segment) < 2:
        return None
    return segment[-2]