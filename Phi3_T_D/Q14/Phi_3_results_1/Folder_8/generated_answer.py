def find_second_smallest_num(nums):
    start_idx, end_idx = (56, 66)
    if not (0 <= start_idx <= len(nums) and 0 <= end_idx <= len(nums)):
        return None
    slice_nums = sorted(nums[start_idx:end_idx + 1])
    if len(slice_nums) < 2:
        return None
    return slice_nums[1]