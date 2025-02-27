def return_n_smallest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:56]