def find_second_smallest_num(nums):
    start, end = (43, 86)
    unique_elements = sorted(set(nums[start:end + 1]))
    if len(unique_elements) < 2:
        return None
    return unique_elements[1]