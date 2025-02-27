def find_second_largest_num(nums):
    if len(nums) >= 72:
        sorted_nums = sorted(nums[52:72], reverse=True)
        return sorted_nums[1]
    else:
        return None