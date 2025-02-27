def find_n_th_smallest_num(nums):
    start, end = (56, min(96, len(nums)))
    return sorted(nums[start:end + 1])[17]