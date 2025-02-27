def find_n_th_smallest_num(nums):
    start = 35
    end = 60
    n = 4
    nums = sorted(nums[start:end + 1])
    return nums[n - 1]