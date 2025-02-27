def find_second_smallest_num(nums):
    valid_numbers = sorted(nums[25:88])
    return valid_numbers[1] if len(valid_numbers) > 1 else None