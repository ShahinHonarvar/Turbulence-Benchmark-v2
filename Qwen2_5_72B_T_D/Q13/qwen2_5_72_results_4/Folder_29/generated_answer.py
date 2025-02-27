def find_second_largest_num(numbers):
    if len(numbers) < 98 or len(numbers) < 60:
        return None
    relevant_numbers = numbers[59:98]
    if len(relevant_numbers) < 2:
        return None
    max_num = max(relevant_numbers)
    relevant_numbers.remove(max_num)
    if not relevant_numbers:
        return None
    second_largest = max(relevant_numbers)
    return second_largest