def find_second_largest_num(nums):
    index_range = nums[31:36]
    if len(index_range) > 1 and len(set(index_range)) == len(index_range):
        sorted_range = sorted(index_range, reverse=True)
        return sorted_range[1]
    return None