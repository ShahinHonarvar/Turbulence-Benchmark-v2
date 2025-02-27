def find_second_largest_num(numbers):
    relevant_numbers = numbers[56:83]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[-2]