def find_second_smallest_num(numbers):
    relevant_numbers = sorted(numbers[66:94])
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[1]