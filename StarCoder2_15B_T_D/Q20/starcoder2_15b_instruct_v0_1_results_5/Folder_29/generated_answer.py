def find_n_th_smallest_num(nums):
    window = nums[20:63]
    window.sort()
    return window[11]