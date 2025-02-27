def find_second_largest_num(nums):
    if len(nums) < 4 or len(nums[33:37]) < 4:
        return None
    sorted_slice = sorted(nums[33:37])
    return sorted_slice[-2]