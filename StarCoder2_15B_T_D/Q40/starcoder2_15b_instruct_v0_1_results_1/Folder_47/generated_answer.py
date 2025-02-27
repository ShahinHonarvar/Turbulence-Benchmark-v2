def return_n_smallest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[-21:]