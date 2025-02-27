def find_second_largest_num(nums):
    index_range = nums[21:98]
    if len(index_range) < 2:
        return None
    sorted_range = sorted(index_range, reverse=True)
    return sorted_range[1]