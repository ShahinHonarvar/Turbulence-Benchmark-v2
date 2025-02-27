def find_n_th_smallest_num(nums):
    if len(nums) < 10 or len(nums) > 10:
        return None
    sorted_nums = sorted(nums[2:10])
    if len(sorted_nums) < 6:
        return None
    return sorted_nums[5]