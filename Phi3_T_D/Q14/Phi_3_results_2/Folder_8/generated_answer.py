def find_second_smallest_num(numbers):
    if 56 <= len(numbers) <= 66:
        second_smallest = sorted(numbers[55:66])[1] if len(set(numbers[55:66])) > 1 else None
        return second_smallest
    return None