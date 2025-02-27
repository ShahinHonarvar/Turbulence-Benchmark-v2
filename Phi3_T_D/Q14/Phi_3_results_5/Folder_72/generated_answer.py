def find_second_smallest_num(numbers):
    relevant_numbers = numbers[82:87]
    unique_numbers = set(relevant_numbers)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(min(unique_numbers))
    return min(unique_numbers)