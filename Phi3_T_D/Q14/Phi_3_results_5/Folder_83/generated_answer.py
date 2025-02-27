def find_second_smallest_num(nums):
    valid_nums = nums[90:201]
    if len(valid_nums) < 2:
        return None
    valid_nums = sorted(set(valid_nums))
    return valid_nums[1] if len(valid_nums) > 1 else None