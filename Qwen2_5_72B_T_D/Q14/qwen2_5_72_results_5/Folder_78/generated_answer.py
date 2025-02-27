def find_second_smallest_num(numbers):
    if len(numbers) < 78 or len(numbers) < 17:
        return None
    sliced_numbers = numbers[17:79]
    if len(sliced_numbers) < 2:
        return None
    first_min = min(sliced_numbers)
    sliced_numbers.remove(first_min)
    second_min = min(sliced_numbers)
    return second_min