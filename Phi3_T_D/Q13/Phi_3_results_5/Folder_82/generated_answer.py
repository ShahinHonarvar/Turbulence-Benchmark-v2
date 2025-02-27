def find_second_largest_num(nums):
    filtered_nums = nums[20:201]
    if len(filtered_nums) < 2:
        return None
    sorted_nums = sorted(filtered_nums, reverse=True)
    return sorted_nums[1]