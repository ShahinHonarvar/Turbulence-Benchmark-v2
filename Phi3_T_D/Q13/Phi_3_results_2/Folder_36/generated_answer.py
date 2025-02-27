def find_second_largest_num(nums):
    unique_numbers = sorted(set(nums[246:751]), reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None