def find_second_smallest_num(nums):
    start, end = (533, min(605, len(nums)))
    filtered_nums = sorted(nums[start:end + 1])
    return filtered_nums[1] if len(filtered_nums) > 1 else None