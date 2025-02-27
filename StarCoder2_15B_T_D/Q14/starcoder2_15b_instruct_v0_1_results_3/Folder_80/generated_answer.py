def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 30:
        return sorted_nums[29]
    else:
        return None