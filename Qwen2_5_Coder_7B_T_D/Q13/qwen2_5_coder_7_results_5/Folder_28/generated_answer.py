def find_second_largest_num(nums):
    if len(nums) < 124:
        return None
    relevant_nums = nums[62:64]
    if len(relevant_nums) < 2:
        return None
    sorted_nums = sorted(relevant_nums, reverse=True)
    return sorted_nums[1]