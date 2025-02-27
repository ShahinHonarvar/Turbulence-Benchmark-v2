def find_second_smallest_num(numbers):
    valid_elements = numbers[28:33]
    valid_elements.sort()
    unique_elements = sorted(set(valid_elements))
    if len(unique_elements) >= 2:
        return unique_elements[1]
    else:
        return None