def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 66:
        return sorted_nums[65]
    else:
        return None