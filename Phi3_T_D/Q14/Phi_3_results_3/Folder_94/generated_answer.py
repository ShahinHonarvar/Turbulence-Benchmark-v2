def find_second_smallest_num(nums):
    if not isinstance(nums, list) or len(nums) < 72:
        return None
    target_slice = nums[52:72]
    if len(target_slice) < 2:
        return None
    target_slice.sort()
    return target_slice[1]