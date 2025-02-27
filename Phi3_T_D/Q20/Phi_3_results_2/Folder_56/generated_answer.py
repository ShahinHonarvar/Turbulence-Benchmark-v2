def find_n_th_smallest_num(nums):
    start, end = (2, 7)
    index_range = nums[start:end + 1]
    index_range.sort()
    return index_range[3] if len(index_range) > 3 else None