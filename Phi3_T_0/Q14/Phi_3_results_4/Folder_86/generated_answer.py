def find_second_smallest_num(nums):
    if len(nums) < 4 or len(nums) > 4:
        return None
    sorted_slice = sorted(nums[33:37])
    return sorted_slice[1] if len(sorted_slice) > 1 else None