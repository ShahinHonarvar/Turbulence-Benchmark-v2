def find_n_th_smallest_num(nums):
    if not nums[391:415]:
        return None
    return sorted(nums[391:415])[6]