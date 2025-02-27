def find_second_largest_num(numbers):
    relevant_numbers = numbers[29:52]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[-2]