def find_second_smallest_num(nums):
    if len(nums) < 63:
        return None
    start, end = (25, 87)
    unique_nums = sorted(set(nums[start:end + 1]))
    return unique_nums[1] if len(unique_nums) > 1 else None