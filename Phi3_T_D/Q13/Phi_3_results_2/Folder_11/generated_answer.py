def find_second_largest_num(numbers):
    start_index = min(37, len(numbers) - 1)
    end_index = min(51, len(numbers) - 1)
    if end_index - start_index < 1:
        return None
    sorted_slice = sorted(numbers[start_index:end_index + 1], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None