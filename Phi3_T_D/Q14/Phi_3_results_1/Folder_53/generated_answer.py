def find_second_smallest_num(nums):
    if not 1 <= len(nums) <= 100:
        raise ValueError('The list must contain 1 to 100 elements.')
    if len(nums) < 2:
        return None
    unique_nums = sorted(set(nums[1:101]))
    return unique_nums[1] if len(unique_nums) > 1 else None