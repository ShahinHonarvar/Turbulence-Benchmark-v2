def find_n_th_smallest_num(nums):
    start_index = 52
    end_index = 88
    sorted_slice = sorted(nums[start_index:end_index + 1])
    return sorted_slice[9]