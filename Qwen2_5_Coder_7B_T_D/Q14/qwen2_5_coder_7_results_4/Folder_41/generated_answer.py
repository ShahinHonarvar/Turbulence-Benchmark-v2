def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sliced_numbers = sorted(numbers[4:5])
    return sliced_numbers[0] if len(sliced_numbers) > 0 else None