def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    tenth_element = numbers[10:11]
    if len(tenth_element) < 2:
        return None
    sorted_tenth = sorted(tenth_element)
    return sorted_tenth[1]