def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 99:
        return None
    relevant_numbers = numbers[56:99]
    if len(relevant_numbers) < 2:
        return None
    unique_numbers = list(set(relevant_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]