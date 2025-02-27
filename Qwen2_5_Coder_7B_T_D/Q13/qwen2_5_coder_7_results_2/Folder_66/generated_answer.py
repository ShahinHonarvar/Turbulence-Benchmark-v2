def find_second_largest_num(nums):
    sub_nums = nums[50:55]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(sub_nums, reverse=True)
    return sorted_nums[1] if len(set(sorted_nums)) > 1 else None