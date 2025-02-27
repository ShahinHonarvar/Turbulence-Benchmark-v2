def find_second_largest_num(nums):
    start_index = 29
    end_index = 79
    target_els = nums[start_index:end_index + 1]
    if len(target_els) < 2:
        return None
    target_els.sort()
    return target_els[-2]