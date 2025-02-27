def find_second_largest_num(numbers):
    selected_numbers = sorted(numbers[75:86], reverse=True)
    return selected_numbers[1] if len(selected_numbers) > 1 else None