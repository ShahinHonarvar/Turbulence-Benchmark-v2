def find_second_largest_num(numbers):
    if len(numbers) < 751 or len(numbers) < 246:
        return None
    relevant_numbers = numbers[246:751]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    if len(relevant_numbers) == 2:
        return relevant_numbers[0]
    else:
        return relevant_numbers[-2]