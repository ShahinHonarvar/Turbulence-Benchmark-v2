def find_n_th_smallest_num(nums):
    start = min(50, len(nums))
    end = min(81, len(nums))
    return sorted(nums[start:end + 1])[5]