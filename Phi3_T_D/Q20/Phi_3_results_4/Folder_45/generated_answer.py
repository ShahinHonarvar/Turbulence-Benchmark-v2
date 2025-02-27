def find_n_th_smallest_num(nums):
    n = 16
    nums.sort()
    return nums[n - 1] if n <= len(nums) else None