def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums)
    n = 4
    smallest_num = sorted_nums[n - 1]
    start_index = 4
    end_index = 8
    return smallest_num