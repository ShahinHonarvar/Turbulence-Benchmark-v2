def find_second_smallest_num(nums):
    index_range = nums[21:98]
    if len(index_range) < 2:
        return None
    unique_nums = sorted(set(index_range))
    return unique_nums[1] if len(unique_nums) > 1 else None