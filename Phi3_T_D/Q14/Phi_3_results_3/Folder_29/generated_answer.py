def find_second_smallest_num(nums):
    filtered_nums = nums[55:99]
    if len(filtered_nums) < 2:
        return None
    sorted_nums = sorted(filtered_nums)
    return sorted_nums[1]