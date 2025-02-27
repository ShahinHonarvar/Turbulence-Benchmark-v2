def find_n_th_smallest_num(nums):
    if 18 <= len(nums) <= 82 and 18 <= 6 <= 82:
        return sorted(nums[18:83])[5]
    return None