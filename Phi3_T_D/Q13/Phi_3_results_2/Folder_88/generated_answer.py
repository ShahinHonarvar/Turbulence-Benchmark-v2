def find_second_largest_num(nums):
    selected_indices = nums[4:9]
    sorted_indices = sorted(selected_indices, reverse=True)
    if len(sorted_indices) > 1:
        return sorted_indices[1]
    return None