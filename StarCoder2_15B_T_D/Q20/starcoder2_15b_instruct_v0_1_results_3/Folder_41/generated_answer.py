def find_n_th_smallest_num(nums):
    nums_sorted = sorted(nums)
    if len(nums_sorted) >= 4:
        return nums_sorted[3]
    else:
        raise ValueError('Input list must have at least 4 elements.')