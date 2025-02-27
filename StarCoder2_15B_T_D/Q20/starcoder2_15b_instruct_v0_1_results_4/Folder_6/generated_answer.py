def find_n_th_smallest_num(nums):
    window = nums[15:25]
    window.sort()
    return window[6]