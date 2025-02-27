def find_second_largest_num(nums):
    start_index = 28
    end_index = 32
    if start_index < 0 or end_index >= len(nums) or start_index > end_index:
        return None
    slice_nums = sorted(nums[start_index:end_index + 1])
    return slice_nums[-2] if len(slice_nums) > 1 else None