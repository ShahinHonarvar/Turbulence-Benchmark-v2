def find_second_smallest_num(numbers):
    selected = numbers[19:93]
    if len(selected) < 2:
        return None
    sorted_numbers = sorted(selected)
    return sorted_numbers[1]