def find_second_smallest_num(numbers):
    if len(numbers) < 85 or len(numbers) < 71:
        return None
    relevant_numbers = numbers[70:85]
    if len(relevant_numbers) < 2:
        return None
    min_num = min(relevant_numbers)
    relevant_numbers.remove(min_num)
    return min(relevant_numbers)