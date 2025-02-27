def find_second_smallest_num(numbers):
    if len(numbers) <= 62:
        return
    section = numbers[17:79]
    unique_section = sorted(set(section))
    if len(unique_section) < 2:
        return None
    return unique_section[1]