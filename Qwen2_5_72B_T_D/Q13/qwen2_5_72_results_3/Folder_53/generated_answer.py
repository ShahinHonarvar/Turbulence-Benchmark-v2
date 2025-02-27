def find_second_largest_num(numbers):
    if not 100 <= len(numbers) >= 201:
        return None
    relevant_numbers = numbers[100:201]
    if len(set(relevant_numbers)) < 2:
        return None
    largest = max(relevant_numbers)
    relevant_numbers.remove(largest)
    second_largest = max(relevant_numbers)
    return second_largest