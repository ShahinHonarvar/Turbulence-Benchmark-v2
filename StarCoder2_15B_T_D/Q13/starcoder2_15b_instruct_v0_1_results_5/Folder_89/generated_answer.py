def find_second_largest_num(nums):
    nums_subset = nums[56:83]
    sorted_nums = sorted(nums_subset, reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None