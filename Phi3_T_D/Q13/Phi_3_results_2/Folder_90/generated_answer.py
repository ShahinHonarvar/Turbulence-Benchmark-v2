def find_second_largest_num(numbers):
    target_numbers = numbers[262:747]
    if len(target_numbers) < 2:
        return None
    largest_num = max(target_numbers)
    target_numbers = [num for num in target_numbers if num != largest_num]
    second_largest_num = max(target_numbers) if target_numbers else None
    return second_largest_num