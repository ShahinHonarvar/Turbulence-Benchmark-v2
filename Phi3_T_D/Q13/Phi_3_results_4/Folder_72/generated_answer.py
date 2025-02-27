def find_second_largest_num(nums):
    segment = nums[29:52]
    if len(segment) < 2:
        return None
    pivot = max(segment)
    segment.remove(pivot)
    return max(segment)