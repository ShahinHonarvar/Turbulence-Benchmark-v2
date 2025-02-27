def find_second_largest_num(nums):
    relevant_slice = nums[64:67]
    if len(relevant_slice) < 2:
        return None
    max_val = max(relevant_slice)
    relevant_slice.remove(max_val)
    return max(relevant_slice) if relevant_slice else None