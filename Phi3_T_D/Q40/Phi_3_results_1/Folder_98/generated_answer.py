def return_n_smallest_chars(s):
    return sorted(list(s), key=lambda char: ord(char), reverse=True)[:68]