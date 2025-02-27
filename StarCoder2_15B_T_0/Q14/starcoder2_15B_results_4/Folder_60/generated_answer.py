def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 58:
        return sorted_nums[57]
    else:
        return None