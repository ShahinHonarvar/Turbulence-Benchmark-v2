def find_n_th_smallest_num(nums):
    try:
        return sorted(nums[58:94])[11]
    except IndexError:
        return None