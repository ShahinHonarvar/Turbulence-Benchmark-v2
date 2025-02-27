def return_n_smallest_chars(chars_string):
    sorted_chars = sorted(chars_string, key=lambda x: ord(x))
    return sorted_chars[-20:]