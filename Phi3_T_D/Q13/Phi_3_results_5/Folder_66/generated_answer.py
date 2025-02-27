def find_second_largest_num(nums):
    begin, end = (50, 54)
    if end - begin >= 2:
        segment = nums[begin:end + 1]
        unique_segment = list(set(segment))
        unique_segment.sort(reverse=True)
        return unique_segment[1] if len(unique_segment) > 1 else None
    return None