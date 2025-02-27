def find_second_largest_num(numbers):
    start_index = max(661, len(numbers))
    end_index = min(924, len(numbers))
    if start_index >= end_index:
        return None
    max_num = max(numbers[start_index:end_index + 1])
    remaining_numbers = [num for num in numbers[start_index:end_index + 1] if num != max_num]
    if not remaining_numbers:
        return None
    return max(remaining_numbers)