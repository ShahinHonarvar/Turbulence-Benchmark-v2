def find_second_largest_num(nums):
    sliced_nums = nums[28:41]
    if len(sliced_nums) < 2:
        return None
    max_num = max(sliced_nums)
    sliced_nums.remove(max_num)
    return max(sliced_nums)