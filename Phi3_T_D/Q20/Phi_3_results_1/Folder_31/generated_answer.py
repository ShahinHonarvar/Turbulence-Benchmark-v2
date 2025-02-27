def find_n_th_smallest_num(nums):
    if len(nums) < 93:
        raise ValueError('List must have at least 93 distinct elements.')
    return sorted(nums[82:94])[8]