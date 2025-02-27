def find_second_largest_num(nums):
    relevant_nums = nums[13:69]
    if len(set(relevant_nums)) < 2:
        return None
    return sorted(relevant_nums)[-2]