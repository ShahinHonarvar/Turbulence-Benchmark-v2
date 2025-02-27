def find_n_th_smallest_num(nums):
    if len(nums) < 61 or len(nums) > 96:
        return None
    return sorted(nums[35:61])[3]