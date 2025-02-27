def find_n_th_smallest_num(nums):
    if 40 <= len(nums) <= 99:
        return sorted(nums[40:99])[5]
    else:
        return None