def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    candidate_numbers = sorted(numbers[19:93])
    unique_numbers = list(dict.fromkeys(candidate_numbers))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]