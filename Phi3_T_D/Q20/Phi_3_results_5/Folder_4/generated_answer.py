def find_n_th_smallest_num(nums):
    if len(nums) < 34:
        return None
    return sorted(nums[33:95])[17]