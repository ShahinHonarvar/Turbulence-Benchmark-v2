def return_n_smallest_chars(string):
    list_of_chars = list(string)
    sorted_chars = sorted(list_of_chars, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:66]