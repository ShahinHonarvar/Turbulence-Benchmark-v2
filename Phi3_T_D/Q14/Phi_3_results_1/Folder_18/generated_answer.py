def find_second_smallest_num(numbers):
    if len(numbers) < 19 or max(numbers[30:49]) < min(numbers[30:49]):
        return None
    return sorted(numbers[30:49])[1]