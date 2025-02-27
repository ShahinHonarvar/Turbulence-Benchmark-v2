def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 43:
        return sorted_nums[42]
    else:
        return None