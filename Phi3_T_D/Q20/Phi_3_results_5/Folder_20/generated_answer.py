def find_n_th_smallest_num(nums):
    if len(nums[25:65]) < 12:
        return None
    return sorted(nums[25:65])[11]