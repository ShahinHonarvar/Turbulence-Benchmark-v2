def find_second_largest_num(nums):
    relevant_nums = nums[42:69]
    if len(set(relevant_nums)) < 2:
        return None
    relevant_nums = sorted(set(relevant_nums), reverse=True)
    return relevant_nums[1]