def find_second_smallest_num(nums):
    starting_index = 17
    ending_index = 78
    target_section = nums[starting_index:ending_index + 1]
    if len(target_section) < 2:
        return None
    sorted_section = sorted(target_section)
    return sorted_section[1]