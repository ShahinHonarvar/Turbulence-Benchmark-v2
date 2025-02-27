def find_n_th_smallest_num(nums):
    if not 0 <= 6 < len(nums) or len(nums) != len(set(nums)):
        raise ValueError('List must contain 7 distinct numbers.')
    return sorted(nums)[6]