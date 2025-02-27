def find_second_smallest_num(nums):
    if len(nums) < 13 or len(nums) > 13:
        return None
    sorted_slice = sorted(nums[28:41])
    return sorted_slice[1] if len(sorted_slice) > 1 else None