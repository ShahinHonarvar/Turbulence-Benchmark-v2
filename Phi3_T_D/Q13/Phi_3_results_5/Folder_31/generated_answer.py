def find_second_largest_num(nums):
    sliced_nums = nums[75:89]
    sorted_nums = sorted(sliced_nums, reverse=True)
    if sorted_nums and sorted_nums[0] != sorted_nums[1]:
        return sorted_nums[1]
    return None