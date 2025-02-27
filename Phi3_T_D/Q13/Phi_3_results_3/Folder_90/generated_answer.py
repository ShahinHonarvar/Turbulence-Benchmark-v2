def find_second_largest_num(nums):
    if 262 <= len(nums) <= 746:
        sorted_nums = sorted(nums[262:747], reverse=True)
        return sorted_nums[1] if len(sorted_nums) > 1 else None
    return None