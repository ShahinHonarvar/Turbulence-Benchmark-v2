def find_n_th_smallest_num(nums):
    start, end, n = (11, 43, 16)
    return sorted(nums[start - 1:end])[n - 1]