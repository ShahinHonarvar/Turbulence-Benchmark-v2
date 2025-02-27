def find_n_th_smallest_num(nums):
    if 58 <= len(nums) <= 82:
        return sorted(nums[58:83])[5]
    else:
        return None