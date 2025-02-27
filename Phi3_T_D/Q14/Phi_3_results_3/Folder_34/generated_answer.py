def find_second_smallest_num(nums):
    valid_numbers = nums[60:201]
    if len(valid_numbers) < 2:
        return None
    return sorted(set(valid_numbers))[1]