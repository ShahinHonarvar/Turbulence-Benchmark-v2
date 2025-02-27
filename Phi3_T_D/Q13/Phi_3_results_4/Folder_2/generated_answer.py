def find_second_largest_num(nums):
    start, end = (15, min(len(nums), 39) + 1)
    sorted_nums = sorted(nums[start:end], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None