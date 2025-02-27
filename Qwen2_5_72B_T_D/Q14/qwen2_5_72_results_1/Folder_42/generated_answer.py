def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(set(numbers[21:98])) < 2:
        return None
    unique_numbers = list(set(numbers[21:98]))
    unique_numbers.sort()
    return unique_numbers[1]