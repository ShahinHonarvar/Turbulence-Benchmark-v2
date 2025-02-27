def find_second_largest_num(nums):
    relevant_nums = nums[1:6]
    if len(relevant_nums) < 2:
        return None
    relevant_nums = sorted(set(relevant_nums))
    if len(relevant_nums) < 2:
        return None
    return relevant_nums[-2]