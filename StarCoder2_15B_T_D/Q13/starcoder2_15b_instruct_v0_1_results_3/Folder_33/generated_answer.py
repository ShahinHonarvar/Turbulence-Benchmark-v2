def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 668:
        return sorted_nums[667]
    else:
        return None