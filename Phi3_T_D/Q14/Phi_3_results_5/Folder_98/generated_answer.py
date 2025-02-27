def find_second_smallest_num(nums):
    filtered_numbers = sorted(nums[6:8])
    return filtered_numbers[1] if len(filtered_numbers) > 1 else None