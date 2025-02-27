def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    return sorted(numbers[36:47])[1] if len(numbers[36:47]) > 1 else numbers[36]