def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) > 201:
        return None
    relevant_numbers = numbers[80:201]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[-2] if len(relevant_numbers) > 1 else None