def find_second_largest_num(nums):
    if len(nums) < 37 or max(nums) is None or min(nums) is None:
        return None
    sub_nums = nums[15:52]
    unique_nums = list(set(sub_nums))
    return sorted(unique_nums)[-2]