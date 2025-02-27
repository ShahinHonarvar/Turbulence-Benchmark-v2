def find_second_smallest_num(numbers):
    relevant_numbers = numbers[68:87]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[1]