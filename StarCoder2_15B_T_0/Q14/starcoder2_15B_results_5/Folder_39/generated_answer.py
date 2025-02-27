def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 28:
        return sorted_nums[28]
    else:
        return None