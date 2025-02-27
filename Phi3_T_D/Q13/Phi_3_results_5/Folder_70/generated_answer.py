def find_second_largest_num(nums):
    relevant_indexes = slice(28, 33)
    sliced_nums = nums[relevant_indexes]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(set(sliced_nums), reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None