def find_second_largest_num(numbers):
    if len(numbers) < 515:
        return None
    start, end = (246, 750)
    numbers = sorted(numbers[start:end + 1])
    return numbers[-2] if len(numbers) >= 2 else None