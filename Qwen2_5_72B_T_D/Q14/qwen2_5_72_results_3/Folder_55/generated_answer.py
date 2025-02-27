def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    tenth_to_tenth = numbers[10:11]
    if len(tenth_to_tenth) < 2:
        return None
    unique_numbers = list(set(tenth_to_tenth))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None