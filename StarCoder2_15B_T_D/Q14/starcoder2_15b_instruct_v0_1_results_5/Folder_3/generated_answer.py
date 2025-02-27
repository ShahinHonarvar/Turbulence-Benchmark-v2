def find_second_smallest_num(nums):
    window = nums[27:56]
    window.sort()
    if len(window) < 2:
        return None
    return window[1]