def find_n_th_smallest_num(nums):
    window = nums[16:72]
    window.sort()
    return window[13]