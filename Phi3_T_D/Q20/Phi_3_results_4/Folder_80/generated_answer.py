def find_n_th_smallest_num(nums):
    if len(nums) < 99:
        raise ValueError('List must contain at least 99 elements')
    start = 30
    end = 98
    nums_slice = sorted(nums[start:end + 1])
    return nums_slice[4]