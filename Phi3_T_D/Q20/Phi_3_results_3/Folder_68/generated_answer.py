def find_n_th_smallest_num(nums):
    if 0 < len(nums) <= 11:
        return sorted(nums)[10]
    else:
        return None