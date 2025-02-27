def find_second_largest_num(numbers):
    selected_numbers = numbers[28:33]
    if len(selected_numbers) < 2:
        return None
    sorted_numbers = sorted(selected_numbers, reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None