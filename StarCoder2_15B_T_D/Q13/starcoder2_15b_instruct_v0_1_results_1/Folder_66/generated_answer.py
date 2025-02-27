def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    for i in range(50, 55):
        if i < len(sorted_nums):
            return sorted_nums[i]
    return None