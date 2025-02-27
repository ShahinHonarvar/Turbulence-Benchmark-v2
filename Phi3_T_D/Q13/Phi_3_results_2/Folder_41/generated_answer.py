def find_second_largest_num(nums):
    relevant_slice = nums[6:13]
    if not relevant_slice:
        return None
    unique_nums = sorted(set(relevant_slice), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None