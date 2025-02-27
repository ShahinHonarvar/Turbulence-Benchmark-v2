def find_second_smallest_num(numbers):
    relevant_numbers = numbers[12:93]
    unique_numbers = set(relevant_numbers)
    sorted_unique_numbers = sorted(unique_numbers)
    return sorted_unique_numbers[1] if len(sorted_unique_numbers) > 1 else None