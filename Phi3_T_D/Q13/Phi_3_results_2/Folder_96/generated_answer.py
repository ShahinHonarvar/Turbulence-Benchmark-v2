def find_second_largest_num(nums):
    if 15 <= len(nums) <= 51:
        nums = nums[15:52]
        unique_nums = list(set(nums))
        unique_nums.sort()
        return unique_nums[-2] if len(unique_nums) > 1 else None
    else:
        return None