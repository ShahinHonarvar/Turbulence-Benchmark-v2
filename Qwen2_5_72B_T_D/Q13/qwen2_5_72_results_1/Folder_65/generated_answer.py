def find_second_largest_num(numbers):
    relevant_numbers = numbers[56:99]
    if len(relevant_numbers) < 2:
        return None
    max_num = max(relevant_numbers)
    relevant_numbers.remove(max_num)
    if relevant_numbers:
        return max(relevant_numbers)
    else:
        return None