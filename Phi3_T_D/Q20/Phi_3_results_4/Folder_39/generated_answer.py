def find_n_th_smallest_num(nums):
    if 47 <= len(nums) <= 89:
        return sorted(nums[47:89 + 1])[6]
    else:
        raise ValueError('List size must be between 47 and 89.')