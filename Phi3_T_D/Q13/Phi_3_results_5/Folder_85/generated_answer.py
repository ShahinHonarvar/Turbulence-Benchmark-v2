def find_second_largest_num(nums):
    selected_slice = nums[6:9]
    if len(selected_slice) < 2:
        return None
    return sorted(selected_slice)[-2]