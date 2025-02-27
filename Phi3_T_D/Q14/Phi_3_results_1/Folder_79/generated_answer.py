def find_second_smallest_num(numbers):
    elements = numbers[1:6]
    elements.sort()
    if len(elements) < 2:
        return None
    return elements[1]