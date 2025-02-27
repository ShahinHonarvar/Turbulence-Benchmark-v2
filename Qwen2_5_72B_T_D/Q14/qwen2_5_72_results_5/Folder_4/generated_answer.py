def find_second_smallest_num(numbers):
    if len(numbers) < 85 or len(numbers) < 71:
        return None
    sliced_numbers = numbers[70:85]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]