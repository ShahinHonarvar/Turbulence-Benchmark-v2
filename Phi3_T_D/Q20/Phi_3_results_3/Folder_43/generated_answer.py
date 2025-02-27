def find_n_th_smallest_num(nums):
    n = 28
    k = 16
    selected_nums = sorted(nums[n:n + 37])
    if k <= len(selected_nums):
        return selected_nums[k - 1]
    return None