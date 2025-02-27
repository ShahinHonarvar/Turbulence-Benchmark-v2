def find_n_th_smallest_num(nums):
    window = nums[21:70]
    window.sort()
    return window[9]