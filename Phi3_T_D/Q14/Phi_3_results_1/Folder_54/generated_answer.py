def find_second_smallest_num(lst):
    relevant_part = lst[68:87]
    if len(relevant_part) < 2:
        return None
    sorted_part = sorted(relevant_part)
    return sorted_part[1]