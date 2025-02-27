def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums)
    sublist = sorted_nums[55:67]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[5]