def find_second_largest_num(nums):
    start, end = (66, min(93, len(nums)))
    unique_numbers = sorted(set(nums[start:end + 1]), reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None