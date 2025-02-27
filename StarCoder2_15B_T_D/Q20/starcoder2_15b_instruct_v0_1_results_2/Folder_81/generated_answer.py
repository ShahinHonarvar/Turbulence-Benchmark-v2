def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums)
    idx = sorted_nums.index(nums[13])
    sorted_nums.pop(idx)
    return sorted_nums[13]