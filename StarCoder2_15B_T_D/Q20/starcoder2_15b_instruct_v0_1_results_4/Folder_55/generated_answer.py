def find_n_th_smallest_num(nums):
    if not nums or len(nums) < 13:
        raise ValueError('Invalid input: the list must be non-empty and have at least 13 elements.')
    if len(set(nums)) != len(nums):
        raise ValueError('Invalid input: the list must contain only distinct numbers.')
    nums.sort()
    return nums[12]