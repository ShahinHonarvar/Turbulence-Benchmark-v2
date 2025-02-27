def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    selected_numbers = numbers[37:77]
    sorted_numbers = sorted(selected_numbers, reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None