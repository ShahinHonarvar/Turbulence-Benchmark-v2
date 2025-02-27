def find_n_th_smallest_num(nums):
    indices = range(1, 10)
    numbers_at_indices = [nums[i] for i in indices]
    return sorted(numbers_at_indices)[6]