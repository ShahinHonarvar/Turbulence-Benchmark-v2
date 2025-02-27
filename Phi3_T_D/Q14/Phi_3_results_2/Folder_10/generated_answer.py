def find_second_smallest_num(numbers):
    if len(numbers[62:93]) < 2:
        return None
    sorted_elements = sorted(numbers[62:93])
    return sorted_elements[1]