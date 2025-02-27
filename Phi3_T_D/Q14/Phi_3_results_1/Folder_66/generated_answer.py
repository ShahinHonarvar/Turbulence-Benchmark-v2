def find_second_smallest_num(nums):
    valid_nums = nums[62:100]
    if len(valid_nums) < 2:
        return None
    unique_nums = sorted(set(valid_nums))
    return unique_nums[1] if len(unique_nums) > 1 else None