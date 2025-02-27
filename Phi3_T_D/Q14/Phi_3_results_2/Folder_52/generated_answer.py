def find_second_smallest_num(nums):
    start, end = (64, 66)
    if not 0 <= start <= end < len(nums):
        return None
    elements = sorted(nums[start:end + 1])
    return elements[1] if len(elements) > 1 else None