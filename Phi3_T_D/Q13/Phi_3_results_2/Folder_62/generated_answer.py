def find_second_largest_num(nums):
    target_window = nums[91:100]
    if len(target_window) < 2 or len(set(target_window)) < 2:
        return None
    return sorted(target_window)[-2]