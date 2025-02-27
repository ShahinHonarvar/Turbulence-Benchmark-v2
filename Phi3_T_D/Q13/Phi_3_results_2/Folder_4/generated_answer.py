def find_second_largest_num(nums):
    if not 12 <= len(nums) <= 93:
        return None
    sliced_nums = nums[12:93]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort(reverse=True)
    return sliced_nums[1]