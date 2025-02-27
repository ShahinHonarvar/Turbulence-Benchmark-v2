def find_n_th_smallest_num(nums):
    if len(nums) < 8:
        return None
    return sorted(nums)[7]