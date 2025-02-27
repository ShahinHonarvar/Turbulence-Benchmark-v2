def find_second_largest_num(numbers):
    start, end = (62, 99)
    relevant_numbers = sorted(numbers[start:end + 1], reverse=True)
    return relevant_numbers[1] if len(relevant_numbers) > 1 else None