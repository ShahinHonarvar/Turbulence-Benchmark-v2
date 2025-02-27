def find_second_smallest_num(numbers):
    unique_numbers = list(set(numbers[26:53]))
    if len(unique_numbers) < 2:
        return None
    else:
        unique_numbers.sort()
        return unique_numbers[1]