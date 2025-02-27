def find_second_smallest_num(numbers):
    start_index = 37
    end_index = 76
    filtered_numbers = sorted(numbers[start_index:end_index + 1])
    return filtered_numbers[1] if len(filtered_numbers) > 1 else None