def find_n_th_smallest_num(nums):
    start, end, target = (16, 72, 14)
    nums[start:end] = sorted(nums[start:end])
    return nums[target - 1]