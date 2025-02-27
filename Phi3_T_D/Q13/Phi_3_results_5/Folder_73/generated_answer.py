def find_second_largest_num(nums):
    relevant_part = nums[19:93]
    if not relevant_part:
        return None
    sorted_numbers = sorted(relevant_part, reverse=True)
    unique_numbers = list(dict.fromkeys(sorted_numbers))
    return None if len(unique_numbers) < 2 else unique_numbers[1]