def find_second_largest_num(numbers):
    start_index, end_index = (max(20, len(numbers)), min(200, len(numbers)))
    if start_index >= end_index:
        return None
    largest, second_largest = (None, None)
    for i in range(start_index, end_index + 1):
        if largest is None or numbers[i] > largest:
            second_largest, largest = (largest, numbers[i])
        elif largest != numbers[i] and (second_largest is None or numbers[i] > second_largest):
            second_largest = numbers[i]
    return second_largest