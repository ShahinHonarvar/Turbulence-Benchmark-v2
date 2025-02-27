def find_second_largest_num(nums):
    start, end = (10, min(100, len(nums)))
    unique_nums = sorted(set(nums[start:end + 1]), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None