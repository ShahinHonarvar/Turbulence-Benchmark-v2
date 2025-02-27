def find_n_th_smallest_num(nums):
    sub_nums = nums[10:101]
    sub_nums.sort()
    return sub_nums[9]