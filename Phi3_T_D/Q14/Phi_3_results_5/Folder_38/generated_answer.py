def find_second_smallest_num(numbers):
    relevant_numbers = numbers[37:52]
    if len(relevant_numbers) < 2:
        return None
    sorted_relevant_numbers = sorted(relevant_numbers)
    return sorted_relevant_numbers[1]