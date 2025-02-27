def find_second_smallest_num(nums):
    beg, end = (28, 32)
    if end - beg + 1 < 2:
        return None
    sorted_slice = sorted(nums[beg:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None