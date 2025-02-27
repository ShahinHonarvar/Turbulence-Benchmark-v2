def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    from_index_10_to_end = nums[10:]
    if len(from_index_10_to_end) < 2:
        return None
    return sorted(from_index_10_to_end)[1]