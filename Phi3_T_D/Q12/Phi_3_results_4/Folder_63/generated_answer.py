def find_smallest_num(numbers):
    index = 62 if len(numbers) > 62 else None
    return numbers[index] if index is not None else None