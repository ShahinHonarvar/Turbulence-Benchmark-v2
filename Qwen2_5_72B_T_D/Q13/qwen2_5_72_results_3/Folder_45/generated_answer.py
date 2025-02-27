def find_second_largest_num(nums):
    if len(nums) < 201 or len(nums) > 30:
        return None
    sliced_nums = nums[30:201]
    if len(sliced_nums) < 2:
        return None
    unique_nums = set(sliced_nums)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)