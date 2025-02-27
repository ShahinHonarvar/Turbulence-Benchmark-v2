def find_second_smallest_num(nums):
    start_index = 75
    end_index = 94
    filtered_nums = nums[start_index:end_index + 1]
    sorted_filtered_nums = sorted(filtered_nums)
    return sorted_filtered_nums[1] if len(sorted_filtered_nums) > 1 else None