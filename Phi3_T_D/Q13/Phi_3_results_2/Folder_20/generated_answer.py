def find_second_largest_num(numbers):
    start_index, end_index = (56, 66)
    if start_index > len(numbers) or end_index <= start_index:
        return None
    relevant_numbers = sorted(numbers[start_index:end_index + 1], reverse=True)
    unique_numbers = list(dict.fromkeys(relevant_numbers))
    return unique_numbers[1] if len(unique_numbers) > 1 else None