def find_second_largest_num(numbers):
    if len(numbers) < 83:
        return None
    section = numbers[56:83]
    section.sort()
    if len(section) < 2:
        return None
    return section[-2]