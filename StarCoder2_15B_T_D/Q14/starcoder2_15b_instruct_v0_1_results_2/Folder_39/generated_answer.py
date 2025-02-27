def find_second_smallest_num(nums):
    window = sorted(nums[28:41])
    return window[1] if len(window) > 1 else None