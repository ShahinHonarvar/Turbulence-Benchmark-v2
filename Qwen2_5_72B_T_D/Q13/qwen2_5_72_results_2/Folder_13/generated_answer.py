def find_second_largest_num(numbers):
    if len(numbers) < 88 or len(set(numbers[25:88])) < 2:
        return None
    unique_numbers = sorted(set(numbers[25:88]), reverse=True)
    return unique_numbers[1]