def find_n_th_smallest_num(nums):
    unique_nums = sorted(set(nums[39:69]))
    return unique_nums[13] if len(unique_nums) >= 14 else None