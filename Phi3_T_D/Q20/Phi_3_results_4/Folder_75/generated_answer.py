def find_n_th_smallest_num(nums):
    n = min(82, len(nums))
    return sorted(nums[18:n])[5]