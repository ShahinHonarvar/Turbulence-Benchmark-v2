def find_second_smallest_num(lst):
    relevant_part = lst[686:987]
    if len(relevant_part) < 2:
        return None
    relevant_part.sort()
    return relevant_part[1]