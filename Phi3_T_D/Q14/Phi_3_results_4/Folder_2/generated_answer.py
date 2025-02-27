def find_second_smallest_num(nums):
    relevant_slice = nums[43:87]
    unique_values = set(relevant_slice)
    if len(unique_values) < 2:
        return None
    return sorted(unique_values)[1]