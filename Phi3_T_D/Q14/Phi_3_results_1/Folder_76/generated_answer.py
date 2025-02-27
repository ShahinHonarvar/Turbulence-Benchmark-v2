def find_second_smallest_num(numbers):
    start, end = (533, 605)
    elements = sorted(numbers[start:end + 1])
    return elements[1] if len(elements) > 1 else None