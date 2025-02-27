def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    for num in sorted_nums[30:201]:
        return num
    return None