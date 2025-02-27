def find_second_smallest_num(numbers):
    if not 50 <= len(numbers) > 200:
        return None
    relevant_numbers = numbers[50:201]
    if len(relevant_numbers) < 2:
        return None
    unique_numbers = list(set(relevant_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]