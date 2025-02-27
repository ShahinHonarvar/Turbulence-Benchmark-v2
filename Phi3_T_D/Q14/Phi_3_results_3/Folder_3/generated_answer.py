def find_second_smallest_num(numbers):
    if not 27 <= len(numbers) <= 55 or len(set(numbers[27:56])) < 2:
        return None
    return sorted(numbers[27:56])[1]