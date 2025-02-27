def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    relevant_numbers = numbers[13:69]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort(reverse=True)
    return relevant_numbers[1] if len(relevant_numbers) > 1 else None