def find_second_largest_num(nums):
    valid_indices = nums[0:8]
    if len(valid_indices) < 2 or len(valid_indices) == len(set(nums[0:8])):
        return None
    return sorted(valid_indices)[-2]