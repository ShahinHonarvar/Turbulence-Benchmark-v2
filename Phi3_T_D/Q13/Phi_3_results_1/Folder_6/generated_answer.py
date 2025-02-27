def find_second_largest_num(nums):
    window_nums = nums[10:67]
    if len(window_nums) < 2:
        return None
    first_max = max(window_nums[0], window_nums[1])
    second_max = min(window_nums[0], window_nums[1])
    for num in window_nums[2:]:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif first_max > num > second_max:
            second_max = num
    return second_max if second_max != float('-inf') else None