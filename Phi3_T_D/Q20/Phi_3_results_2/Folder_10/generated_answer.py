def find_n_th_smallest_num(nums):
    n = 18
    unique_nums = sorted(set(nums[56:97]))
    return unique_nums[n - 1] if n <= len(unique_nums) else None