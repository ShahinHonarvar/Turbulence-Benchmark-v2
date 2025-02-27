def find_n_th_smallest_num(nums):
    if len(nums) < 13:
        return None
    return sorted(nums)[:13][-1]