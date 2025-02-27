def find_second_smallest_num(numbers):
    start_index, end_index = (30, 200)
    filtered_numbers = sorted(numbers[start_index:end_index + 1])[:2]
    return filtered_numbers[1] if len(filtered_numbers) > 1 else None