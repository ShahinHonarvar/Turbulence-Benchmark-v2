def find_n_th_smallest_num(nums):
    if len(nums) < 7 or len(nums) > 7:
        return None
    return sorted(nums)[6]