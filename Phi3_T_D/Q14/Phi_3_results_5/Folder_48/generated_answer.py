def find_second_smallest_num(nums):
    relevant_section = sorted(set(nums[246:751]))
    return relevant_section[1] if len(relevant_section) > 1 else None