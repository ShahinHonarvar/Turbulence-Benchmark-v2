def find_second_largest_num(nums):
    relevant_slice = nums[32:36]
    if len(relevant_slice) < 2:
        return None
    return sorted(relevant_slice)[-2]