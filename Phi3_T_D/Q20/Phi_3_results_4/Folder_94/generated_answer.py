def find_n_th_smallest_num(nums):
    slice_nums = nums[57:71]
    sorted_nums = sorted(slice_nums)
    if len(sorted_nums) >= 6:
        return sorted_nums[5]
    else:
        return None