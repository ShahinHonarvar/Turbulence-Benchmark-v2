def find_n_th_smallest_num(nums):
    window = nums[11:92]
    window.sort()
    return window[12]