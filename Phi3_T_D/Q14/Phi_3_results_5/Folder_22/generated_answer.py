def find_second_smallest_num(nums):
    valid_indices = nums[40:201]
    if len(set(valid_indices)) < 2:
        return None
    sorted_nums = sorted(set(valid_indices))
    return sorted_nums[1]