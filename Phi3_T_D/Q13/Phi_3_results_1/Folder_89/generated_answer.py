def find_second_largest_num(numbers):
    if not 56 <= len(numbers) <= 82:
        return None
    elements = numbers[56:83]
    if len(set(elements)) < 2:
        return None
    elements.sort()
    return elements[-2]