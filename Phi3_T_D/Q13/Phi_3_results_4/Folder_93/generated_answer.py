def find_second_largest_num(nums):
    if len(nums) < 90:
        return None
    target = nums[75:95]
    unique_nums = sorted(set(target), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None