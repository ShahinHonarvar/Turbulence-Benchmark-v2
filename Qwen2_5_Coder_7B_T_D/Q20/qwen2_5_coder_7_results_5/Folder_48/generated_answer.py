def find_n_th_smallest_num(nums):
    subset = nums[127:849]
    subset.sort()
    return subset[9]