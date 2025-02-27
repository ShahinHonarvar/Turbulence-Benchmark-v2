def find_second_smallest_num(numbers):
    if len(numbers) < 79 or len(set(numbers[62:79])) < 2:
        return None
    unique_numbers = sorted(set(numbers[62:79]))
    return unique_numbers[1]