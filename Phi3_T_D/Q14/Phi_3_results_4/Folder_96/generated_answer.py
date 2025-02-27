def find_second_smallest_num(numbers):
    valid_section = numbers[50:201]
    if len(valid_section) < 2:
        return None
    sorted_section = sorted(valid_section)
    return sorted_section[1] if len(sorted_section) > 1 else None