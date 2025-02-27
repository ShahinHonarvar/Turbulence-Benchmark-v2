def find_n_th_smallest_num(nums):
    start_index = 23
    end_index = 65
    sorted_slice = sorted(nums[start_index:end_index + 1])
    return sorted_slice[7]