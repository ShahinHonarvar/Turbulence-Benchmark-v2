def find_second_largest_num(nums):
    start_index, end_index = (37, 51)
    if end_index - start_index < 2:
        return None
    sorted_section = sorted(nums[start_index:end_index + 1], reverse=True)
    return sorted_section[1] if len(sorted_section) > 1 else None