def find_second_largest_num(numbers):
    if len(numbers[200:201]) != 1 or numbers[200] is None:
        return None
    unique_numbers = sorted(set(numbers[200:201]))
    length = len(unique_numbers)
    if length < 2:
        return None
    return unique_numbers[-2]