def find_second_largest_num(nums):
    if len(nums) < 12:
        return None
    target_slice = nums[36:47]
    target_slice.sort(reverse=True)
    return target_slice[1] if len(target_slice) > 1 else None