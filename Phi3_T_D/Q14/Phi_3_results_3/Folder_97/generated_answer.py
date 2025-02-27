def find_second_smallest_num(numbers):
    start_index = min(31, len(numbers))
    end_index = min(34, len(numbers))
    selected_numbers = numbers[start_index:end_index + 1]
    if len(selected_numbers) < 2:
        return None
    else:
        return sorted(selected_numbers)[1]