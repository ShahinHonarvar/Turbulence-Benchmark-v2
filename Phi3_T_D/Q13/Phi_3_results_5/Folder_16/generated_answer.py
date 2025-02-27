def find_second_largest_num(nums):
    selected_slice = nums[33:37]
    selected_slice.sort()
    if selected_slice:
        return selected_slice[-2]
    return None