def find_n_th_smallest_num(nums):
    start, end, n = (35, 60, 4)
    subset = sorted(nums[start:end + 1])[:n]
    return subset[-1]