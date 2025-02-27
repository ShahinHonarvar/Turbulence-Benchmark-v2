def find_n_th_smallest_num(nums):
    n = 4
    target_range = nums[56:71]
    target_range.sort()
    return target_range[n - 1]