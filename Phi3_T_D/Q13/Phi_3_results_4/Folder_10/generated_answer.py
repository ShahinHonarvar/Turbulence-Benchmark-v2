def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    sublist = nums[25:60]
    unique_nums = set(sublist)
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)