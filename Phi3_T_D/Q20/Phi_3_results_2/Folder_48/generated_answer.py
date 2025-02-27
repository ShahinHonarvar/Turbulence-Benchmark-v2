def find_n_th_smallest_num(nums):
    index_start, index_end = (127, min(848, len(nums)))
    relevant_numbers = nums[index_start:index_end + 1]
    return sorted(relevant_numbers)[9]