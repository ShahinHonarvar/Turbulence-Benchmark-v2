def find_second_largest_num(nums):
    sorted_nums = sorted(nums[262:747], reverse=True)
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None