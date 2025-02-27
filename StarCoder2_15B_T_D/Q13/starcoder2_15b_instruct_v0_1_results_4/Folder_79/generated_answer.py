def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 4:
        return sorted_nums[3]
    else:
        return None