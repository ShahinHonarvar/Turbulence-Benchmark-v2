def find_second_smallest_num(numbers):
    if len(numbers) < 151:
        return None
    numbers = sorted(numbers[50:201])
    return numbers[1] if len(numbers) >= 2 else None