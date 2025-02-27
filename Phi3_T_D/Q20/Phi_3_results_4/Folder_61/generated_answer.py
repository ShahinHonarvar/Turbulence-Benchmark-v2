def find_n_th_smallest_num(nums):
    return sorted(nums[:10])[9] if len(nums) >= 10 else None