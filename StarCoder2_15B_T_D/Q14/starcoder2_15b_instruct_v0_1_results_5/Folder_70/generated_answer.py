def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 40:
        return sorted_nums[39]
    else:
        return None