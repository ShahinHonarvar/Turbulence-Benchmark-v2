def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    relevant_numbers = numbers[10:11]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[1]