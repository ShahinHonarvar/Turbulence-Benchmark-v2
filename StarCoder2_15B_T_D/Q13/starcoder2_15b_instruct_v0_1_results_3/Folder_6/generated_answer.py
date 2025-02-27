def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    for i in range(10, 67):
        if sorted_nums[i] != sorted_nums[i + 1]:
            return sorted_nums[i]
    return None