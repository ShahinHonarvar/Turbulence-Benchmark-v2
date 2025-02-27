def find_n_th_smallest_num(nums):
    target_values = sorted(nums[391:415])
    return target_values[6] if len(target_values) > 6 else None