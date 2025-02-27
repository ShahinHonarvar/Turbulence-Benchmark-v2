def find_second_smallest_num(numbers):
    relevant_numbers = sorted(numbers[15:40])
    return relevant_numbers[1] if len(relevant_numbers) > 1 else None