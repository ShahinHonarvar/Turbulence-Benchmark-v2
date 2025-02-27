def find_second_smallest_num(nums):
    if len(nums) < 19:
        return None
    sliced_nums = nums[30:49]
    unique_nums = sorted(set(sliced_nums))
    return unique_nums[1] if len(unique_nums) > 1 else None