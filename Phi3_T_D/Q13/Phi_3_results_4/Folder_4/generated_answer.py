def find_second_largest_num(numbers):
    if not 12 <= len(numbers) <= 101:
        return None
    relevant_numbers = numbers[11:93]
    if len(relevant_numbers) < 2:
        return None
    largest = max(relevant_numbers)
    relevant_numbers.remove(largest)
    second_largest = max(relevant_numbers)
    return second_largest