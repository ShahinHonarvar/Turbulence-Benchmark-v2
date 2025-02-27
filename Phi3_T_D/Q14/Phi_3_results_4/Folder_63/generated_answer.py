def find_second_smallest_num(nums):
    target_range = nums[56:83]
    if len(target_range) < 2:
        return None
    sorted_unique_nums = sorted(set(target_range))
    return sorted_unique_nums[1] if len(sorted_unique_nums) > 1 else None