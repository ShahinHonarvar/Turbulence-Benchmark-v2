def find_second_largest_num(nums):
    if len(nums) < 13:
        return None
    start_index = min(13, len(nums))
    end_index = min(68, len(nums)) + 1
    if end_index - start_index < 2:
        return None
    window = nums[start_index:end_index]
    window.sort(reverse=True)
    return window[1]