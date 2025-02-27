def find_second_largest_num(nums):
    selected_nums = nums[4:9]
    if len(selected_nums) < 2:
        return None
    sorted_selected_nums = sorted(selected_nums, reverse=True)
    return sorted_selected_nums[1]