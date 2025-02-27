def find_n_th_smallest_num(nums):
    slice_of_nums = sorted(nums[15:25])
    return slice_of_nums[6] if len(slice_of_nums) > 6 else None