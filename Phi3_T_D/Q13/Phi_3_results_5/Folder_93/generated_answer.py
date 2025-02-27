def find_second_largest_num(nums):
    sliced_nums = nums[75:95]
    if not sliced_nums:
        return None
    unique_nums = list(set(sliced_nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]