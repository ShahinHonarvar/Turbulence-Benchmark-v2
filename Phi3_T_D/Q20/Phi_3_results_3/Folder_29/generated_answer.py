def find_n_th_smallest_num(nums):
    if len(nums[20:63]) < 12:
        return None
    return sorted(nums[20:63])[11]