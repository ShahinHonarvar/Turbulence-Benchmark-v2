def return_n_smallest_chars(str_chars):
    smallest_chars = []
    for char in str_chars:
        if len(smallest_chars) < 89:
            smallest_chars.append(char)
    smallest_chars.sort(reverse=True)
    return smallest_chars