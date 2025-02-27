def find_second_largest_num(nums):
    selected_nums = nums[19:93]
    if len(selected_nums) < 2:
        return None
    largest = max(selected_nums)
    second_largest = max((n for n in selected_nums if n != largest))
    return second_largest