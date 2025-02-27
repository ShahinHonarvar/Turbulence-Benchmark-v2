def find_second_smallest_num(nums):
    if len(nums) < 4 or len(nums) > 4:
        return None
    if nums[31] == nums[32] == nums[33] == nums[34]:
        return None
    sorted_slice = sorted(nums[31:35])
    return sorted_slice[1] if len(set(sorted_slice)) > 1 else None