def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    second_smallest = sorted(numbers[20:31])[1] if len(numbers[20:31]) > 1 else None
    return second_smallest