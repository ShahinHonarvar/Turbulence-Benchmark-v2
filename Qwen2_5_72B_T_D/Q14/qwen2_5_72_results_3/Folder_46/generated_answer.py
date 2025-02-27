def find_second_smallest_num(numbers):
    if len(numbers) < 69 or len(numbers) < 14:
        return None
    sliced_numbers = numbers[13:69]
    if len(sliced_numbers) < 2:
        return None
    min_num = min(sliced_numbers)
    sliced_numbers.remove(min_num)
    return min(sliced_numbers) if sliced_numbers else None