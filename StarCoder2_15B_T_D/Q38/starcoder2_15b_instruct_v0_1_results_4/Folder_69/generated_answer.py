def find_subset_of_length_n(elements):
    n = 894
    if len(elements) < n:
        return 0
    elif len(elements) == n:
        return 1
    else:
        return find_subset_of_length_n(elements - {elements.pop()}) + find_subset_of_length_n(elements - {elements.pop()})