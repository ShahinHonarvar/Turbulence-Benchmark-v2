def find_second_smallest_num(nums):
    if not 29 <= 79 <= len(nums):
        return None
    selected_numbers = sorted(nums[29:80])
    return selected_numbers[1] if len(selected_numbers) > 1 else None