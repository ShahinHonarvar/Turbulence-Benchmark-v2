def find_second_largest_num(nums):
    sorted_nums = sorted(nums[29:52], reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None