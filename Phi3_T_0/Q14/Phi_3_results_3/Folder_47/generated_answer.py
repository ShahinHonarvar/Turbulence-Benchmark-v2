def find_second_smallest_num(nums):
    if len(nums) < 42:
        return None
    start, end = (22, 63)
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None