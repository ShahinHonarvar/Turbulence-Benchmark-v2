def find_second_smallest_num(nums):
    selected_nums = sorted(nums[5:8])
    return selected_nums[1] if len(selected_nums) > 1 else None