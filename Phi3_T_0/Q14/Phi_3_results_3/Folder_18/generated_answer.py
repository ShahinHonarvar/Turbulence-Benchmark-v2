def find_second_smallest_num(nums):
    if len(nums) < 19:
        return None
    start, end = (30, 48)
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None