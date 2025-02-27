def find_n_th_smallest_num(nums):
    if len(nums) < 79:
        return None
    return sorted(nums[63:80])[10]