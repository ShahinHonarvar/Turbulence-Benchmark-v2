def find_second_smallest_num(numbers):
    start_index, end_index = (29, 51)
    if len(numbers) <= end_index + 1:
        return None
    filtered_numbers = sorted(numbers[start_index:end_index + 1])
    return filtered_numbers[1] if len(filtered_numbers) > 1 else None