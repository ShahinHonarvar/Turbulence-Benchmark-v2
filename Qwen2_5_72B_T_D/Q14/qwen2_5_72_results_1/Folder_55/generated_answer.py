def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    tenth_index_elements = [numbers[10]]
    if len(tenth_index_elements) < 2:
        return None
    first_min = min(tenth_index_elements)
    tenth_index_elements.remove(first_min)
    second_min = min(tenth_index_elements) if tenth_index_elements else None
    return second_min