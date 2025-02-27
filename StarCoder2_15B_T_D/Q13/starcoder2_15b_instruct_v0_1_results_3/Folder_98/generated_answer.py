def find_second_largest_num(nums):
    if len(nums) > 6:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[1]
    else:
        return None