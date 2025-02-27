def find_second_largest_num(nums):
    start, end = (100, 200)
    filtered_nums = sorted(set(nums[start:end + 1]), reverse=True)
    return filtered_nums[1] if len(filtered_nums) > 1 else None