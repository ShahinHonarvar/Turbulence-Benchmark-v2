def find_second_smallest_num(numbers):
    if len(numbers) < 100 or len(numbers) > 10:
        return None
    numbers = numbers[10:101]
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]