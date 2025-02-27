def find_n_th_smallest_num(nums):
    start, end, k = (11, 91, 13)
    return sorted(nums[start - 1:end])[k - 1]