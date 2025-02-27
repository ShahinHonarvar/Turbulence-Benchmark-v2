def find_n_th_smallest_num(nums):
    window = nums[75:92]
    window.sort()
    return window[10]