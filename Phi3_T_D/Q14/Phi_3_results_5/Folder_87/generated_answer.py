def find_second_smallest_num(nums):
    start, end = (22, min(len(nums), 89))
    unique_nums = sorted(set(nums[start:end]))
    return unique_nums[1] if len(unique_nums) > 1 else None