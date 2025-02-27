def find_second_smallest_num(nums):
    start, end = (29, 51)
    if end > len(nums) or start < 0:
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None