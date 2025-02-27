def find_second_largest_num(nums):
    relevant_slice = nums[56:83]
    if len(relevant_slice) < 2:
        return None
    sorted_slice = sorted(relevant_slice, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None