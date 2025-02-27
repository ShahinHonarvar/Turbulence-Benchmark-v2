def find_second_smallest_num(lst):
    valid_elements = [x for i, x in enumerate(lst) if i >= 40 and i <= 200]
    if len(valid_elements) < 2:
        return None
    valid_elements.sort()
    return valid_elements[1]