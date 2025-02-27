def find_second_largest_num(nums):
    if 262 <= len(nums) <= 746:
        selected_range = nums[262:747]
        if len(set(selected_range)) > 1:
            return sorted(set(selected_range))[-2]
    return None