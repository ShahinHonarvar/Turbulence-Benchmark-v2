def find_second_smallest_num(numbers):
    begin, end = (28, 40)
    if end < begin or begin >= len(numbers) or end >= len(numbers):
        return None
    numbers = sorted(numbers[begin:end + 1])
    return numbers[1] if len(numbers) > 1 else None