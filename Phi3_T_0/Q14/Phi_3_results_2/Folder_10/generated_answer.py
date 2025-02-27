def find_second_smallest_num(nums):
    if len(nums) < 30:
        return None
    start, end = (62, 92)
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None