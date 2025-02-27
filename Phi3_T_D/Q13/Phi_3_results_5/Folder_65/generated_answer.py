def find_second_largest_num(nums):
    selected_slice = nums[56:99]
    if not selected_slice:
        return None
    sorted_slice = sorted(selected_slice, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None