def find_second_smallest_num(nums):
    trimmed_nums = nums[62:100]
    if len(trimmed_nums) < 2:
        return None
    sorted_nums = sorted(trimmed_nums)
    return sorted_nums[1]