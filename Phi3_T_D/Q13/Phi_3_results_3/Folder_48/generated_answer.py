def find_second_largest_num(numbers):
    if 533 <= len(numbers) <= 605:
        valid_numbers = numbers[533:606]
        if len(set(valid_numbers)) < 2:
            return None
        return sorted(set(valid_numbers))[-2]
    return None