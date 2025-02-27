def find_second_largest_num(nums):
    if len(nums) < 747 or len(nums) < 263:
        return None
    sliced_nums = nums[262:747]
    if len(sliced_nums) < 2:
        return None
    unique_nums = list(set(sliced_nums))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]