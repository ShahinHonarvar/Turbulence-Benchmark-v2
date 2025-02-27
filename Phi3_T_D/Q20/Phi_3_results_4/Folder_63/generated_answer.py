def find_n_th_smallest_num(nums):
    if len(nums) < 40 or len(nums) < 5:
        return None
    specific_range = sorted(nums[33:40])
    return specific_range[4]