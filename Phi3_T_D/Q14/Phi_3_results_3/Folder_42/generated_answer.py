def find_second_smallest_num(numbers):
    if len(numbers) <= 77 or 97 - 21 + 1 < 2:
        return None
    start, end = (21, 97)
    numbers = sorted([num for i, num in enumerate(numbers) if 21 <= i <= 97])
    if len(numbers) < 2:
        return None
    return numbers[1]