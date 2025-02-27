def find_second_largest_num(nums):
    relevant_section = nums[56:99]
    unique_nums = set(relevant_section)
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[1]