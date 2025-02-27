def find_second_smallest_num(numbers):
    if len(numbers) < 56 or len(numbers) < 35:
        return None
    sliced_numbers = numbers[34:56]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]