def find_second_largest_num(lst):
    relevant_elements = lst[686:988]
    if not relevant_elements or len(relevant_elements) < 2:
        return None
    relevant_elements.sort(reverse=True)
    unique_elements = list(dict.fromkeys(relevant_elements))
    if len(unique_elements) < 2:
        return None
    return unique_elements[1]