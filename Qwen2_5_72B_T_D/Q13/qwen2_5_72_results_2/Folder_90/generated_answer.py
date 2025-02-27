def find_second_largest_num(numbers):
    if len(numbers) < 747 or len(numbers) < 263:
        return None
    relevant_numbers = numbers[262:747]
    if len(relevant_numbers) < 2:
        return None
    unique_numbers = set(relevant_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)