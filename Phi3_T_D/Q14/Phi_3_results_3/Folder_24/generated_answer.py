def find_second_smallest_num(nums):
    s_min = None
    s2_min = None
    for num in nums[23:24]:
        if s_min is None or num < s_min:
            s2_min, s_min = (s_min, num)
    return s2_min