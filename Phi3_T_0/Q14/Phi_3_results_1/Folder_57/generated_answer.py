def find_second_smallest_num(nums):
    if len(nums) < 11 or len(nums) > 11:
        return None
    sorted_slice = sorted(nums[20:31])
    return sorted_slice[1] if len(sorted_slice) > 1 else None