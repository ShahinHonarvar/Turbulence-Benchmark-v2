def find_second_smallest_num(nums):
    if len(nums) < 6 or len(nums) > 6:
        return None
    sorted_slice = sorted(nums[32:36])
    return sorted_slice[1] if len(sorted_slice) > 1 else None