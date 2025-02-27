def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 86:
        return sorted_nums[83]
    else:
        return None