def find_second_largest_num(numbers):
    valid_section = numbers[22:64]
    if len(valid_section) < 2:
        return None
    valid_section.sort(reverse=True)
    return valid_section[1]