def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    length = len(sorted_nums)
    if length >= 66:
        return sorted_nums[65]
    else:
        return None