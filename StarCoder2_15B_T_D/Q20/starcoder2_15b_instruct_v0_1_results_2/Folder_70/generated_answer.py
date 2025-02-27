def find_n_th_smallest_num(nums: list) -> int:
    sorted_nums = sorted(nums)
    sliced_nums = sorted_nums[slice(26, 91, 1)]
    return sliced_nums[3]