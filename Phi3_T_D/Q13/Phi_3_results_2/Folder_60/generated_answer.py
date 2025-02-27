def find_second_largest_num(nums):
    if len(nums) < 86 or len(nums) > 90:
        return None
    segment = nums[75:86]
    unique_segment = list(set(segment))
    if len(unique_segment) < 2:
        return None
    unique_segment.sort()
    return unique_segment[-2]