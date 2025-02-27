def find_n_th_smallest_num(nums):
    start, end, n = (59, 74, 4)
    return sorted(nums[start:end + 1])[n - 1]