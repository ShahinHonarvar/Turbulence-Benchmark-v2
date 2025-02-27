def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    sliced_numbers = numbers[34:56]
    if len(set(sliced_numbers)) < 2:
        return None
    first_min = min(sliced_numbers)
    sliced_numbers.remove(first_min)
    second_min = min(sliced_numbers)
    return second_min