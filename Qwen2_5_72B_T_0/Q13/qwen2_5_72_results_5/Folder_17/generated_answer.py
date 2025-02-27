def find_second_largest_num(numbers):
    if len(numbers) < 79 or len(numbers) < 63:
        return None
    sliced_numbers = numbers[62:79]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]