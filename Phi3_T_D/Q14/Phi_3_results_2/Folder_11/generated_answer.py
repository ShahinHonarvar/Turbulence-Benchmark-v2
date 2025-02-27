def find_second_smallest_num(numbers):
    start_index, end_index = (66, 93)
    if start_index > len(numbers) or end_index > len(numbers):
        return None
    numbers = numbers[start_index:end_index + 1]
    if len(numbers) < 2:
        return None
    first_min = min(numbers)
    numbers.remove(first_min)
    return min(numbers)