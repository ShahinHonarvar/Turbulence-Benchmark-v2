def find_second_largest_num(numbers):
    if len(numbers) < 65 or len(numbers) > 65:
        return None
    relevant_numbers = numbers[14:65]
    if len(relevant_numbers) < 2:
        return None
    max_num = max(relevant_numbers)
    relevant_numbers.remove(max_num)
    second_max = max(relevant_numbers) if relevant_numbers else None
    return second_max