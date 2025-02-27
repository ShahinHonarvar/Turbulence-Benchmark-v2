def find_n_th_smallest_num(nums):
    subset = nums[30:301]
    subset.sort()
    return subset[14]