def find_second_smallest_num(nums):
    filtered_nums = nums[60:201]
    if len(filtered_nums) < 2:
        return None
    min_num = min(filtered_nums)
    filtered_nums.remove(min_num)
    return min(filtered_nums, default=None)