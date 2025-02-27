def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    numbers = numbers[1:6]
    numbers = sorted(set(numbers))
    return numbers[-2] if len(numbers) > 1 else None